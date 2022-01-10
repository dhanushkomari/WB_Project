from re import search
from django.http.response import HttpResponse
from django.shortcuts import render
from App.models import HandSettings, VBSettings, MobileSettings, HandSettings
from .serializers import HandSettingsSerializer, VBSettingsSerializer, MobileSettingsSerializer, MobileSpeakerSerializer
from api import serializers

from rest_framework.response import Response
from rest_framework.decorators import api_view

import time

# Create your views here.
@api_view(['GET'])
def CallDetailsView(request, username):
    data = MobileSettings.objects.filter(username = username).latest('pk')
    serializers = MobileSettingsSerializer(data, many = False)
    return Response(serializers.data)

@api_view(['GET'])
def VBDetailsViews(request, username):
    data = VBSettings.objects.filter(username = username).latest('pk')
    serializers = VBSettingsSerializer(data, many = False)
    return Response(serializers.data)

@api_view(['POST'])
def updateSpeaker(request, username):
    d = MobileSettings.objects.filter(username = username).latest('pk')
    serializers = MobileSpeakerSerializer(instance = d, data = request.POST)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

###############  HAND APIs  ###########################

@api_view(['GET'])
def LatestHandSettingsView(request, username):
    try:
        h = HandSettings.objects.filter(username = username).latest('pk')
        serializers = HandSettingsSerializer(h, many = False)
        return Response(serializers.data)
    except:
        return HttpResponse('No data found')

@api_view(['POST'])
def updatehandSettingsview(request, username):
    try:
        h = HandSettings.objects.filter(username = username).latest('pk')
    except:
        h = HandSettings.objects.create(time = time.time(), bot_name = 'default', username = request.user.username)
    
    serializers = HandSettingsSerializer(instance = h, data = request.POST)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

    



