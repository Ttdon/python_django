from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    #return HttpResponse ("<h1>Hello World</h1>") #string of html code
    return render(request,"home.html",{})


def contact_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "contact.html", {})
    return HttpResponse("<h1>Contact Person</h1>")


def about_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request.user)
    my_context={
        "my_text" : "thid is sbout us",
        "my_number": 123,
        "my_list": [123,4242,12313,"Abc"]
    }

    return render(request, "about.html", my_context)

def social_view(request,*args,**kwargs):
    print(args, kwargs)
    print(request)
    return render(request, "social.html", {})
    return HttpResponse("<h1>Social Person</h1>")