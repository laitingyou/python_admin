from django.http import HttpResponse
from info.models import info
import json
def infodb(request):
    # data=info(name='lai',city='gz')
    # data.save()
    # list = info.objects.all()

    return HttpResponse()
