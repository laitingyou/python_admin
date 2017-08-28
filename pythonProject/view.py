from django.http import HttpResponse
from django.shortcuts import render
import json
from Constroller.Socket import Socket
def hello(request):
    sockets=Socket();
    content={}
    return render(request,'index.html',content)
def home(request):
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    jsons=json.dumps(data)
    context={}
    context['hello']='nima'
    return HttpResponse(jsons)
