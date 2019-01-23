from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    url('', csrf_exempt(views.home), name="move_blob_home"),
]