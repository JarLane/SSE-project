
import zipfile
from urllib.parse import urlparse
#from xml.etree.ElementTree import tostring

import requests
import ssl
import json
import socket
from datetime import datetime, timezone
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import time



url = "https://localhost:33333"



def check_certificate_expiry(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    port = parsed_url.port if parsed_url.port else 443
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.create_connection((hostname, port)) as conn:
        with context.wrap_socket(conn, server_hostname=hostname) as ssl_conn:

            cert_der = ssl_conn.getpeercert(binary_form=True)

            cert = x509.load_der_x509_certificate(cert_der, default_backend())

            cert_expiry = cert.not_valid_after_utc.replace(tzinfo=timezone.utc)

            if cert_expiry < datetime.now(timezone.utc):
                print(f"The SSL certificate for {url} has expired.")
                path = "SSL_Problem.json"
                zipPath = f"SSL.zip"
                with open(path, "w") as file:
                    json_data = {'Error': 'The SSL certificate has expired.'}
                    json.dump(json_data, file, indent=2)
                with zipfile.ZipFile(zipPath, "w") as zip:
                    zip.write(path)


            else:
                print(f"The SSL certificate for {url} is valid. Expires on: {cert_expiry}")




def ping():

    try:
        response = requests.get(url)
        if response.status_code == 200:
            pass
        else:
            raise Exception(response.json())
    except Exception as e:
        path = "problem.json"
        zipPath = "alert.zip"
        with open(path,"w") as file:
            json_data = {'Error' : str(e)}
            json.dump(json_data, file, indent=2)
        with zipfile.ZipFile(zipPath,"w") as zip:
            zip.write(path)


app_settings = {
    "url": "https://localhost:33333",
    "email": "user@example.com",
    "time_setting": "1",
    "run": ""
}

json_data = json.dumps(app_settings, indent=4)

def running():
    run = app_settings["run"]
    time_setting = float(app_settings["time_setting"])
    if run == "true":
        while True:

            ping()
            check_certificate_expiry(app_settings["url"])
            time.sleep((time_setting * 60))
    else:
        print("Goodbye")
