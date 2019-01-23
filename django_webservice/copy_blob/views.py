# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from miscutils import copy_blob
from miscutils import log_to_file
import json

# Create your views here.
def home(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode('utf-8'))
        response = copy_blob.copy_blob(**received_json_data)
        log_to_file.main(received_json_data, response)
        success = isinstance(response, dict)
        
        if success:
            return JsonResponse({"status": "success"}, status=200)
        else:
            return JsonResponse({"status": "failure"}, status=400)
    else:
        return JsonResponse({"foo":"bar"})

