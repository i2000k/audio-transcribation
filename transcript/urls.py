from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_transcribation', views.transcribate, name='transcribate')
]