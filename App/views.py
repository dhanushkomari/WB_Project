from django.http.response import Http404, HttpResponse
from django.shortcuts import render, redirect
from .models import Bot, MobileSettings, VBSettings
from django.http import HttpResponse
from time import time

# Create your views here.


# Home View .......................................
def HomeView(request):
    return render(request, 'App/home.html')


# Bot Selection View................................
def SelectBotView(request, id):
    if request.method == 'POST':
        if 'call_button' in request.POST:
            b = Bot.objects.get(id = id)
            mob_no = request.POST['mob_no']
            username = request.user.username
            try:        
                m = MobileSettings.objects.filter(username = username).latest('pk')
                m.username = username
                m.bot_name = b.bot_name
                m.mob_no = mob_no
                m.time = time()
                m.save()                
            except:
                m = MobileSettings.objects.create(mob_no = mob_no, time = time(), username = username)

            return render(request, 'App/call_detail.html', {'b':b, 'mob_no':mob_no, 'm':m})


    else:
        b = Bot.objects.get(id = id)
        return render(request, 'App/bot_detail.html', {'b':b})



# Speaker On View......................................
def SpeakerONStautsView(request, id):
    b = Bot.objects.get(id = id)
    try:
        m = MobileSettings.objects.filter(username = request.user.username).latest('pk')        
        m.speaker = True
        m.time = time()
        mob_no = m.mob_no
        m.save()        
    except:
        pass
    return render(request, 'App/call_detail.html', {'b':b, 'mob_no':mob_no, 'm':m})


# Speaker Off View......................................
def SpeakerOFFStatusView(request, id):
    b = Bot.objects.get(id = id)
    try:
        m = MobileSettings.objects.filter(username = request.user.username).latest('pk')
        m.speaker = False
        m.time = time()
        mob_no = m.mob_no
        m.save()
    except:
        pass
    return render(request, 'App/call_detail.html', {'b':b, 'mob_no':mob_no, 'm':m})


# Select Voice Bot View...................................
def SelectVBBotView(request, id):
    b = Bot.objects.get(id = id)
    try:
        v = VBSettings.objects.filter(username = request.user.username).latest('pk')
        v.time = time()
        v.save()
    except:
        v = VBSettings.objects.create(username = request.user.username, time = time())

    return render(request, 'App/VB_detail.html', {'v':v, 'b':b})


# Bot Status View............................................
def Botstatus(request, id):
    b = Bot.objects.get(id = id)
    m = MobileSettings.objects.filter(username = request.user.username).latest('pk')
    if m.bot_name == b.bot_name:
        return render(request, 'App/call_detail.html', {'b':b, 'mob_no':m.mob_no, 'm':m})
    else:
        b = ''
        mob_no = 'Not Found'
        m = ''

        return render(request, 'App/call_detail.html', {'b':b, 'mob_no':m.mob_no, 'm':m})




     