from re import search
from django.shortcuts import render
from App.models import VBSettings, MobileSettings
from .serializers import VBSettingsSerializer, MobileSettingsSerializer, MobileSpeakerSerializer
from api import serializers

from rest_framework.response import Response
from rest_framework.decorators import api_view

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

