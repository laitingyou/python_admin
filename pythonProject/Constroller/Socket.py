from django.http import HttpResponse
class Socket:
    def __init__(self):
        print (self)
    def bind(self):
        return HttpResponse(234234)
