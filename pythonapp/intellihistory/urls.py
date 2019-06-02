from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recordSession', views.recordSession, name='recordSession'),
    path('summary', views.summary, name='summarizePage'),
    path('ppt', views.ppt, name='ppt'),
    path('pdf', views.pdf, name='pdf'),
    path('keywords', views.keywords, name='keywords'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('search', views.search, name='search'),
    path('session', views.session, name='session'),
    path('summarise', views.summary, name='summarise')
]