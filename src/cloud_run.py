import requests


payload = {"hash_tag": "music"}

url = "https://europe-west2-tiktokapi-364416.cloudfunctions.net/run_download"

r = requests.post(url, data=payload)