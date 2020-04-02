import os
from secrets import token_hex
import urllib.request
from tempfile import NamedTemporaryFile

from django.http import HttpResponse
from django.core.files.base import File
from django.db import models

# Create your models here.
class CroppingSession(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    @classmethod
    def create_from_url(cls, url):
        req = urllib.request.Request(url,
                data=None,
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                }
        )
        response = urllib.request.urlopen(req)
        if response.info().get_content_maintype() == 'image':
            hex_token = token_hex(4)
            extension = response.info().get_content_subtype()
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(response.read())
            img_temp.flush()
            session = cls.objects.create()
            session.image.save(f"{hex_token}-{session.id}.{extension}", File(img_temp))
            return session
        else:
            return HttpResponse(status=400)


    @property
    def filetype(self):
        return os.path.splitext(self.image.name)[1][1:]

    @property
    def filename(self):
        return os.path.splitext(self.image.name)[0]



    def __str__(self):
        return f"Crop N{self.id}"
