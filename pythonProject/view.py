from django.http import HttpResponse
from django.shortcuts import render
import json
import httplib
data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
jsons=json.dumps(data)
def hello(request):
    http_client=httplib.HTTPConnection('baidu.com',80,timeout=20)
    http_client.request('GET', '')
    r = http_client.getresponse()
    return HttpResponse(r)

def home(request):


