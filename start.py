import zipfile
import requests
import ssl
import json

url = "change this url"
response = requests.get(url)
if response.status_code == 200:
    pass
    else
