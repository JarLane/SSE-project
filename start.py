import zipfile
import requests
import ssl
import json

url = "http://localhost:33333"
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
