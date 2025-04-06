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
        path = "problem.json"
        with open(path,"w") as file:
            json_data = response.json()
            json.dump(json_data, file, indent=2)
except Exception as e:
    path = "problem.json"
    with open(path,"w") as file:
        json_data = {'Error' : str(e)}
        json.dump(json_data, file, indent=2)
