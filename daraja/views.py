import requests
import simplejson
from requests.auth import HTTPBasicAuth
import base64
from datetime import datetime
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from django.conf import settings
from rest_framework.views import APIView
from products.serializers import ProductSerializer
from . import helpers
from api import common
Common=common.CommonContainer()
logger=Common._get_logger()



def GenerateAccessToken():
  #token=helpers.Generatetoken()
  consumer_key=settings.CONSUMER_KEY
  consumer_secret=settings.CONSUMER_SECRET
  token=helpers.Helpers().generate_token(key=consumer_key,secret=consumer_secret)
  return token
  #return data

def MakePayment(request):
  access_token=GenerateAccessToken()
  BusinessShortCode="174379"

  pass_key=settings.PASS_KEY
  callback_url="%s%s" %(settings.NGROK,'daraja/confirm_payment')
  timestamp=datetime.today().strftime("%Y%m%d%H%M%S")
  to_encode="%s%s%s" %(BusinessShortCode, pass_key, timestamp)
  Password = base64.b64encode(to_encode.encode('ascii'))
  api_url=settings.LIPA_NA_MPESA_URL

  headers = { "Authorization": "Bearer %s" % access_token }
  request = {
    "BusinessShortCode": BusinessShortCode,
    "Password": Password,
    "Timestamp": timestamp,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "2500",
    "PartyA": "254708374149",
    "PartyB": BusinessShortCode,
    "PhoneNumber": "254708374149",
    "CallBackURL": callback_url,
    "AccountReference": "UM4ETY67F",
    "TransactionDesc": "Test payment"
  }

  response = requests.post(api_url, json = request, headers=headers,verify=False)
  res=response.json()
  logger.info(str(type(res)))
  logger.info (res.get("ResponseCode"))
  logger.info (res.get("ResponseDescription"))
  return HttpResponse(res.get("ResponseCode"))

def CofirmPayment(request):
  return HttpResponse(request)


