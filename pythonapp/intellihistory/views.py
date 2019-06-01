from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import pandas as pd
from langdetect import detect
from tqdm import tqdm_notebook

from intellihistory.classes import SessionUrl, UserSession
from intellihistory.modelling import summarizePage

# Use a service account
cred = credentials.Certificate('intelli-history-af3a3c220a14.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Create your views here.
def index(request):
        return HttpResponse("This index controller works!")

@csrf_exempt
def recordSession(request):
    # records the different urls visited in a single session
    if(request.method == 'POST'):
        url = request.POST.get('url')
        title = request.POST.get('title')
        session_id = request.POST.get('session-id')
        session_url = SessionUrl(url=url, title=title)
        # updating the session object in firestore
        db.collection(u'sessions').document(session_id).set({
                u'urls': {
                        title: url
                }
        }, merge=True)        
        return HttpResponse("This controller works too")
    else:
        return HttpResponse("This does not work")


def modelSession(request):
        # creates 
        data = pd.read_csv('articles_bbc_2018_01_30.csv')
        print(data.shape)
        data = data.dropna().reset_index(drop=True)
        print(data.shape)
        print(data.head())
        tqdm_notebook().pandas()
        data['lang'] = data.articles.progress_map(detect)

@csrf_exempt
def summary(request):
        if request.method == 'POST':
                url = request.POST.get('url')
                summary = summarizePage(url)
                return HttpResponse(summary)
        else:
                return HttpResponse("The method is not POST")
        








        