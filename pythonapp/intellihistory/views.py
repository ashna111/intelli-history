from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1 import ArrayRemove, ArrayUnion

import pandas as pd
from langdetect import detect
from tqdm import tqdm_notebook

from intellihistory.classes import SessionUrl, UserSession
from intellihistory.modelling import summarizePage, makePPT, makePDF, getKeywords

# Use a service account
cred = credentials.Certificate('intelli-history-af3a3c220a14.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Create your views here.
def index(request):
        return HttpResponse("This index controller works!")

def dashboard(request):


        return render(request,'intellihistory/dashboard.html')

@csrf_exempt
def recordSession(request):
    # records the different urls visited in a single session
    if(request.method == 'POST'):
        url = request.POST.get('url')
        present_url = request.POST.get('present-url')
        session_id = request.POST.get('session-id')
        session_url = SessionUrl(url=url, present_url=present_url, session_id=session_id)
        # updating the session object in firestore
        child = {
                u'name': url,
                u'parent': present_url
        }

        session_ref = db.collection('sessions').document(session_id)
        session = session_ref.get()
        session = session.to_dict()
        path = ''
        for key, value in session:
                if key == 'parent' and value == 'null':
                        path = ''
                elif key == 'name' and value == present_url:
                        path = path + 'children'
                elif session[key] != present_url:
                        path = path + 'children'

        print(path)
        
        db.collection(u'sessions').document(session_id).update({
                [u'tree.' + path]: ArrayUnion([child])
        })        
        return HttpResponse("This controller works too")
    else:
        return HttpResponse("This does not work")



@csrf_exempt
def summary(request):
        if request.method == 'POST':
                url = request.POST.get('url')
                summary = summarizePage(url)
                return HttpResponse(summary)
        else:
                return HttpResponse("The method is not POST")

@csrf_exempt
def ppt(request):
        if request.method == 'POST':
                url = request.POST.get('url')
                summary = summarizePage(url)
                makePPT(summary)
                filename = 'content.pptx'

                with open(filename, 'rb') as f:
                        response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')
                        response['Content-Disposition'] = 'attachment; filename=' + filename
                        response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.presentationml.presentation; charset=utf-16'
                        return response
        else:
                return HttpResponse("ppt controller does not work")

@csrf_exempt
def pdf(request):
        if request.method == 'POST':
                url = request.POST.get('url')
                summary = summarizePage(url)
                makePDF(summary)
                filename = 'content.pdf'

                with open(filename, 'rb') as f:
                        response = HttpResponse(f.read(), content_type='application/pdf')
                        response['Content-Disposition'] = 'attachment; filename=' + filename
                        response['Content-Type'] = 'application/pdf; charset=utf-16'
                        return response
        else:
                return HttpResponse("pdf controller not working")

@csrf_exempt
def keywords(request):
        if request.method == 'POST':
                url = request.POST.get('url')
                keywords = getKeywords(url)
                return HttpResponse(keywords)

        else:
                return HttpResponse("this does not work")

        








        