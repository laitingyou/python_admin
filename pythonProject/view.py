from django.http import HttpResponse
from django.shortcuts import render
import json
from Constroller.Socket import MyHTMLParser
def hello(request):
    content={}
    return render(request,'index.html',content)
def home(request):
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    jsons=json.dumps(data)
    parser = MyHTMLParser()

    return HttpResponse(parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>'))
