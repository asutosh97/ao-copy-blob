# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import datetime

from django.shortcuts import render
from django.http import JsonResponse

from miscutils import copy_blob

# Create your views here.
def home(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode('utf-8'))
        response = copy_blob.copy_blob(**received_json_data)

        # print to console so that its saved in the log file.
        log_data = {
                "request": request, 
                "response": response, 
                "timestamp":str(datetime.datetime.now())
        }
        print("\n\nBlob-Copy-Report :- {}\n\n".format(json.dumps(log_data)))
        
        success = isinstance(response, dict)
        
        if success:
            return JsonResponse({"status": "success"}, status=200)
        else:
            return JsonResponse({"status": "failure"}, status=400)
    else:
        return JsonResponse({"foo":"bar"})

