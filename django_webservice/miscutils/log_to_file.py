import os
import json
import datetime

from google.cloud import storage

from . import constants

def download_log_file():
    storage_client = storage.Client.from_service_account_json(constants.KEYPATH)
    bucket = storage_client.get_bucket(constants.BUCKET_NAME)
    blob = bucket.get_blob(constants.LOGFILE_NAME)
    if blob:
        blob.download_to_filename(constants.LOGFILE_NAME)

def upload_log_file():
    storage_client = storage.Client.from_service_account_json(constants.KEYPATH)
    bucket = storage_client.get_bucket(constants.BUCKET_NAME)
    blob = bucket.blob(constants.LOGFILE_NAME)
    blob.upload_from_filename(constants.LOGFILE_NAME)

def log_to_file(request, response):
    log_data = {
                "request": request, 
                "response": response, 
                "timestamp":str(datetime.datetime.now())
                }
    with open(constants.LOGFILE_NAME, 'a') as f:
         f.write(json.dumps(log_data) + "\n\n")

def main(request, response):
    download_log_file()
    log_to_file(request, response)
    upload_log_file()
    os.remove(constants.LOGFILE_NAME)