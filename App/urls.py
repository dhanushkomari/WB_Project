from django.urls import path
from . import views

app_name = 'App'

urlpatterns = [
    path('', views.HomeView, name = 'home'),
    path('bot/<str:id>', views.SelectBotView, name = 'select-bot'),
    path('speaker/on/<str:id>', views.SpeakerONStautsView, name = 'speaker-on'),
    path('speaker/off/<str:id>', views.SpeakerOFFStatusView, name = 'speaker-off'),

    path('vbot/<str:id>', views.SelectVBBotView, name = 'select-vbot'),
    path('bot-status/<str:id>', views.Botstatus, name = 'bot-status'),

]
