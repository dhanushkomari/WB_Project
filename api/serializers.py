from rest_framework.fields import ModelField
from App.models import VBSettings, MobileSettings
from rest_framework import serializers

class VBSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VBSettings
        fields = '__all__'

class MobileSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileSettings
        fields = '__all__'

class MobileSpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileSettings
        fields = ('speaker', )