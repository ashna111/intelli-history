from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recordSession', views.recordSession, name='recordSession')
]