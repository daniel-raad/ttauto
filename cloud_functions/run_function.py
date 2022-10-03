
import requests

# http  unauthenticated  endpoint to call
url = "http://localhost:8080"

# the input json payload
param = {"hash_tags":"daniel"}

# post your response
r = requests.post(url, json=param)

# print results
print(r.content)