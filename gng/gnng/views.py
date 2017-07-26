from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.http import Http404
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.http import Http404
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template import loader
import logging
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
# Create your views here.
import json
import http.client
from time import sleep
from twilio.rest import Client
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import os.path
import sys
import webbrowser
from random import randint

import json
try:
    import apiai
except ImportError:
    sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
)


def notifviewer(request):

    conn = http.client.HTTPSConnection("data.heather77.hasura-app.io")

    payload = "{ \"type\" : \"select\", \n        \"args\" : {\n          \"table\" : \"testgng\",\n          \"columns\" : [\"date\",\"time\",\"alert\",\"status\"]\n        \t\n        }\n      }\n\n\n"

    headers = {
        'authorization': "Bearer cf8sohcugy2hx5si4vz4i98culqj6pak",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "2cbcbde0-a035-9017-de33-f199fbcc3961"
        }

    conn.request("POST", "/v1/query", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    

    arrord = json.loads(data.decode("utf-8"))
    ordarr = []
    print("arrord=",arrord)
    print("arrord0=",arrord[0].values())
    list_values = [v for v in arrord[0].values()]
    print("list_values=",list_values)
    ordarr2=[]
    cou =  ""
    nam = ""
    qua = ""
    pri = ""
    ordnu = ""
    stat = ""
    tot=""
    for i in arrord:
        ordarr=[]

        print("--------------------",i)
        

        ordarr.append(i["date"])
        ordarr.append(i["time"])
        ordarr.append(i["alert"])
        ordarr.append(i["status"])

        print("status=",i["status"])
        ordarr2.append(ordarr)
    t = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    conn = http.client.HTTPSConnection("data.heather77.hasura-app.io")

    payload = "{  \"type\" : \"insert\",\n\n        \"args\" : {\n\n            \"table\" : \"testgng\",\n\n          \"objects\"   : [\n\n            {\n\n              \"date\"  : \"4/5/17\",\n\n              \"time\" :\""+t+"\",\n\n              \"alert\" : \"The infant is crying\",\n              \"status\": \"active\"\n            }\n\n          ]\n\n         \n\n        }\n\n     }"

    headers = {
        'authorization': "Bearer cf8sohcugy2hx5si4vz4i98culqj6pak",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "56872e8a-6a16-b0cf-1ef0-ff151217a2a7"
        }

    conn.request("POST", "/v1/query", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

    print("append=",ordarr2)
    context = {'ordarr':ordarr2}
    account_sid = "AC7f7f485965c422ccd1e1b8105d4cf64a"
    # Your Auth Token from twilio.com/console
    auth_token  = "d2bb53c1963c14fac11455c0fbeb9c32"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
    to="+919884558142", 
    from_="+12016547925",
    body="Attend to your child!")

    print(message.sid)

    return render(request, 'gnng/notifviewer.html',context)



def docchatviewer(request):
    i=0
    CLIENT_ACCESS_TOKEN = '0d9107da62e246ac81ad736e76e5ee77'
    context = {'display':'Hey! You can ask me any question you like about child care!'}

    if(request.POST.get("sendmsg")):
        
        
        query = (request.POST.get('rep'))
        ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

        request1 = ai.text_request()

        request1.lang = 'en'  

        request1.query = query

        
        response = request1.getresponse()
        
        responsestr = response.read().decode('utf-8')
        
        response_obj = json.loads(responsestr)

        print(response_obj["result"]["fulfillment"]["speech"])
        
        context = {'display':response_obj["result"]["fulfillment"]["speech"]}

        intentnm = response_obj["result"]["metadata"]["intentName"]
        
        
    return render(request, 'gnng/docchatviewer.htm',context)





