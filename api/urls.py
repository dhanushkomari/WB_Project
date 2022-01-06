from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('call-api/<str:username>', views.CallDetailsView),
    path('vb-api/<str:username>', views.VBDetailsViews),
    path('call-api/<str:username>/speaker/update', views.updateSpeaker),
]
