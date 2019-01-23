from google.cloud import storage

from . import constants

def copy_blob(source_bucket_name, source_blob_name, destination_bucket_name, destination_blob_name=None):
    try:
        storage_client = storage.Client.from_service_account_json(constants.KEYPATH)
        source_bucket = storage_client.get_bucket(source_bucket_name)
        source_blob = source_bucket.get_blob(source_blob_name)
        destination_bucket = storage_client.get_bucket(destination_bucket_name)
        copied_blob = source_bucket.copy_blob(source_blob, destination_bucket, destination_blob_name)
        return copied_blob._properties
    except Exception as e:
        return repr(e)
        
