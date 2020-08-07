from celery import shared_task
from django.template.loader import render_to_string
from django.core import mail
from accounts.models import User
from viewed.settings import BASE_URL
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from accounts.api.tokens import account_activation_token
from chat.views import createNode, deleteNode, updateNode
from posts.models import *
from authy.api import AuthyApiClient

# authy_api = AuthyApiClient('MG90955d0e460f3ca2f60f08f45d6f4e85')
authy_api = AuthyApiClient('a2DsvlbdX6M7pnQgG8faX7IcUgyUrFTH')
from rest_framework_jwt.settings import api_settings
import random
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from common.common import send_prize_notification
from notification.models import Notifications

@shared_task(track_started=True)
def send_email_verify_mail(user_id):
    user_obj = User.objects.get(id=user_id)

    subject = 'Activate Your Viewed Account'
    to = user_obj.email
    plain_message = None
    from_email = 'Viewed <webmaster@localhost>'
    message_text = render_to_string('account_activation/account_activation_email.html', {
        'user': user_obj,
        'domain': BASE_URL,
        'uid': urlsafe_base64_encode(force_bytes(user_obj.pk)).decode(),
        'token': account_activation_token.make_token(user_obj),
    })
    mail.send_mail(subject, plain_message, from_email, [to], html_message=message_text)
    print('done')
    return 'success..!!'

@shared_task(track_started=True)
def send_phone_verify_otp(country_code, mobile_number):
    request = authy_api.phones.verification_start(mobile_number, country_code,
    									via='sms', locale='en')
    if request.content['success'] == True:
        return 'successfully send message'
    else:
        return 'faild to send message' + request.content['message']

@shared_task(track_started=True)
def create_user_node(first_name, last_name, id, profile_image):
    createNode(first_name, last_name ,id, profile_image)
    return 'successfully created user node'

@shared_task(track_started=True)
def update_user_node(first_name, last_name, id, profile_image):
    updateNode(first_name, last_name ,id, profile_image)
    return 'successfully updated user node'

@shared_task(track_started=True)
def delete_user_node(id):
    deleteNode(id)
    return 'successfully created user node'

@shared_task(track_started=True)
def select_winners(comp_id):
    print('start123')
    comp_post_obj = CompetitionPost.objects.get(post__id=comp_id)
    print(comp_post_obj.id)
    print(comp_post_obj)
    entered_user_list = CompetitionEnteredUsers.objects.filter(post__id=comp_id).values_list('entered_by', flat=True)
    no_of_winners = int(comp_post_obj.no_of_winners)
    print( entered_user_list)

    if len(entered_user_list) > no_of_winners:
        winners = random.sample(entered_user_list, no_of_winners)
    else:
        winners = entered_user_list
    print('start2')
    winner_obj = CompetitionWinners.objects.create(post=comp_post_obj.post)
    winner_obj.winners.add(*winners)

    android_user_qs = User.objects.filter(id__in =winners, device_type ='1')
    ios_user_qs = User.objects.filter(id__in =winners, device_type ='2')

    ## send user notification
    data = {
        'notificationType':'1',
        'post_id':comp_post_obj.id,
        'message': 'You won the competition',
        'title': 'Wow',
    }
    if android_user_qs.exists():
        res = send_prize_notification(list(android_user_qs.values_list('device_token', flat=True)),'1',data)
        print(res,'android')
    if ios_user_qs.exists():
        res = send_prize_notification(list(ios_user_qs.values_list('device_token', flat=True)), '2', data)
        print(res,'ios')

    if comp_post_obj.post.created_by.profile_image:
        image = comp_post_obj.post.created_by.profile_image.url
    else:
        image = ''

    all_users = (android_user_qs | ios_user_qs).distinct()

    # save in DB

    for user in all_users:
        Notifications.objects.create(type='1',message='You won the competition',title='Wow', image=image,
                                     post_id = comp_post_obj,user = user)

    print('end')
    return 'end'

@shared_task(track_started=True)
def send_action_notification(type, post_id, user_id):
    """
    1-prize winner
    2-Post like
    3-share
    4-comment
    5-like comment

    """

    user = User.objects.get(id=user_id)
    post_obj = Post.objects.get(id=post_id)


    if user.profile_image:
        image = user.profile_image.url
    else:
        image = ''

    if type==2:
        message = '{} {} liked your post.'.format(user.first_name,user.last_name)
    elif type==3:
        message = '{} {} shared your post.'.format(user.first_name, user.last_name)
    elif type==4:
        message = '{} {} commented on your post.'.format(user.first_name,user.last_name)
    else:
        message = '{} {} liked your comment.'.format(user.first_name, user.last_name)

    Notifications.objects.create(type=type, message=message, title='Viewed', image=image,
                                     post_id_actions = post_obj, user = post_obj.created_by)

    data = {
        'notificationType': type,
        'post_id': post_id,
        'message': message,
        'title': 'Viewed',
    }

    #send_prize_notification([post_obj.created_by.device_token], post_obj.created_by.device_type, data)
    
    from pyfcm import FCMNotification
    fcm_server_key = 'AAAAXz8hx0E:APA91bHuM-ypd_NCV0xIA3b4kVd61Jjh3Yi1JVGbjBCfdaDvO6rT4XwwopiOymw456D553hbT0To8CpAWvI-mh-IPWQoVYXw55mtC5BDcyuHNk-VJc2nte-RINoL5ykxrKCwj1qTRGws'
    push_service=FCMNotification(api_key=fcm_server_key)
    registration_id=post_obj.created_by.device_token
    message_title="Viewed App Notification"
    message_body=message
    result=push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    print(result)

    return 'success'


'''
My work------------------------
'''
# from pyfcm import FCMNotification
# @shared_task(track_started=True)
# def send_action_notification1():
#     #Number Varification
#     # authy_api = AuthyApiClient('a2DsvlbdX6M7pnQgG8faX7IcUgyUrFTH')
#     # mobile_number = '8787632296'
#     # country_code = '+91'
#     # request = authy_api.phones.verification_start(mobile_number, country_code,
#     # 									via='sms', locale='en')
#     # if request.content['success'] == True:
#     #     m = 'successfully send message.'
#     # else:
#     #     m = 'faild to send message' + request.content['message']
#     # print(m)APA

#     #Push Notification
#     fcm_server_key = 'AAAAXz8hx0E:APA91bHuM-ypd_NCV0xIA3b4kVd61Jjh3Yi1JVGbjBCfdaDvO6rT4XwwopiOymw456D553hbT0To8CpAWvI-mh-IPWQoVYXw55mtC5BDcyuHNk-VJc2nte-RINoL5ykxrKCwj1qTRGws'
#     push_service=FCMNotification(api_key=fcm_server_key)
#     registration_id="djFrHwMI0og:APA91bFg2xKXJymtCwAvAjkBX8QbtUtirlqieHMtyE1E_q4mrlhh0bs1R-EgNU2oJl8P3SCR0phJ8r3BRt1UvHMDxo_t2rMw85Hd-12pT0OTRSx6pdGQtkmCMFJFWnSs973VbUnm4C5B"
#     message_title="Viewed App Sample Notification"
#     message_body='HELLO..!! FROM Viewed'
#     result=push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
#     print(result)


# from celery.decorators import periodic_task
# @periodic_task(run_every=10.0)
# def every_ten_seconds():
    # push_service=FCMNotification(api_key="AAAAl8py_xM:APA91bEk2dxBMHfwAaDMJXCh0DbIwjGcoAHHEB0bdy8rH2gduLmFVTURDw8h_ZwfGHlHPQ88cN2vC4wD-fFzN12xzrsEY4WG6ri8ZKgqcZmcjharggi4F0NnXZwC0PeGaJRGPVMKk4g3")
    # push_service=FCMNotification(api_key="AAAAXz8hx0E:APA91bHuM-ypd_NCV0xIA3b4kVd61Jjh3Yi1JVGbjBCfdaDvO6rT4XwwopiOymw456D553hbT0To8CpAWvI-mh-IPWQoVYXw55mtC5BDcyuHNk-VJc2nte-RINoL5ykxrKCwj1qTRGws")
    # registration_id="fTtT_a9dtQU:APA91bH8RaNc2netvyaVqawYqumBzRyvFDFhmLy_8givTliKyebH0tCap1aDeUwRvanL6sBm-fBWsa_qvvcnv3ZBksyEFC9WKXu4tWAUbatI7PdXwPkS4zemELvYZKsVTSEB9G2wvSdT"
    # message_title="Viewed App Sample Notification"
    # message_body='HELLO..!! FROM Viewed'
    # result=push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    # print(result)
    # print("This runs in every 10 seconds")

    # authy_api = AuthyApiClient('jofGCIjJDNjl2z1jkk2N0qRA2FGdOur9')
    # mobile_number = '8787632296'
    # country_code = '+91'

    # request = authy_api.phones.verification_start(mobile_number, country_code,
    # 									via='sms', locale='en')
    # if request.content['success'] == True:
    #     return 'successfully send message'
    # else:
    #     return 'faild to send message' + request.content['message']
    # print('hello')
    # return 'hello'