# ao-copy-blob
A Django webapp that basically copies a blob from one bucket to another.

### Constant Configuration (Not required if deploying in GCP Compute Engine Instance)
Go to the file `django_webservice/miscutils/constants.py` to set the constants to their appropriate values

```python3
KEYPATH = "path to the service_account_credentials.json file"
```

### Dependencies
All the python dependencies that are required are included in the requirements.txt file and procedure for installation is given in the installation section. But, since the code is tested on `python3`, it is recommended to have python3 installated on the system. And for isolating the project environment, it is recommended to have `virtualenv` installed.

### Installation and Running the webapp

```bash
git clone https://github.com/asutosh97/ao-copy-blob-and-log.git
cd ao-copy-blob-and-log
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python django_webservice/manage.py runserver
```

This will run the webapp at `http://127.0.0.1:8000`

### Sample POST Request
Use something like POSTMAN for making a post request to `http://127.0.0.1:8000/copy_blob/` endpoint.

#### HEADERS
`"Content-Type: application/json"`

#### BODY
```json
{
    "source_bucket_name": "b-ao-intern-test1", 
    "source_blob_name": "kitten.png", 
    "destination_bucket_name": "b-ao-intern-test2", 
    "destination_blob_name": "kitten.png"
}
```

Alternatively, you can also make use of the commandline utility cURL to make the POST request.

```bash
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"source_bucket_name": "b-ao-intern-test1", "source_blob_name": "kitten.png", "destination_bucket_name": "b-ao-intern-test2", "destination_blob_name": "kitten.png"}' \
    http://127.0.0.1:8000/copy_blob/  
```
