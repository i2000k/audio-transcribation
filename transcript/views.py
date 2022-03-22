from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core.files.storage import default_storage

from .utils import transcription

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(None, request))

def transcribate(request):
    if request.method == "POST":
      file = request.FILES['file']
      default_storage.save(file.name, file)
      text = transcription(file.name)
    return JsonResponse({"text":text})
