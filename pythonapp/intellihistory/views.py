from django.shortcuts import render
from django.http import HttpResponse

from .models import SessionUrl, UserSession

# Create your views here.
def recordSession(request):
    # records the different urls visited in a single session
    if(request.method == 'POST'):
        session_url = SessionUrl(request.POST)
        