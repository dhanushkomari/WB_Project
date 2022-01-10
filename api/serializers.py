from rest_framework.fields import ModelField
from App.models import VBSettings, MobileSettings, HandSettings
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

class HandSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandSettings
        fields = '__all__'