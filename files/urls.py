from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
        path('create/', csrf_exempt(views.TestView.as_view()))
]
