from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    template=loader.get_template("main/index.html")
    context ={
        'today': datetime.now(),
        'app_name': "Super.Todas"

    }
    return render(request,'main/index.html',context=context)
    # return HttpResponse(template.render(context,request))
