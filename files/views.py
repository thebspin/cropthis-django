from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import CroppingSession

import urllib.request
import base64
# Create your views here.
class TestView(View):

    def post(self, request):
        url = request.POST.get('url')
        session = CroppingSession.create_from_url(url)
        response = {'status':200, 'media':request.build_absolute_uri(session.image.url), 'filename':session.filename, 'filetype':session.filetype}
        return JsonResponse(response)
