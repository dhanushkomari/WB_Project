from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('call-api/<str:username>', views.CallDetailsView),
    path('vb-api/<str:username>', views.VBDetailsViews),
    path('call-api/<str:username>/speaker/update', views.updateSpeaker),

    path('hand/latest/<str:username>', views.LatestHandSettingsView),
    path('hand/update/<str:username>', views.updatehandSettingsview)

]
