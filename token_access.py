import requests
import json


client_id = "26a7f6c5-ed01-47fc-86f5-fc242d50b7a4"
client_secret = "c5ed2280-19ee-4631-9461-3ba3cd5598ad"
redirect_url = "https://localhost"
scope = "https://graph.microsoft.com/.default"
url = "https://login.microsoftonline.com/84f7d290-fa35-41a8-a902-ca1e8f447eb4/oauth2/v2.0/token?client_id="+client_id+"&client_secret="+client_secret+"&redirect_url="+redirect_url+"&scope="+scope

payload='grant_type=client_credentials&client_id=26a7f6c5-ed01-47fc-86f5-fc242d50b7a4&client_secret=mm47Q~iFD78P56MtRHBae2DKUpXdN1QTHWsa5&scope=https%3A%2F%2Fgraph.microsoft.com%2F.default'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'esctx=AQABAAAAAAD--DLA3VO7QrddgJg7Wevr8OjXKZaogjQw-Wr7ZzMvl9s0Klo52reX0Y4adD75LFlA5qlh3njEkeAdPQpa3zYFeBowvSlqAtmCzDFTjy-BM7YYwUeEWePUKRz8CtIyrJVcZmiVak1_hQAhRtgcMKe0PYioeR5km_V38ukNltohHiWcqmD43tFmEkcXB3T4EEsgAA; fpc=Ao9Dpk3oc2hIljIygdiJLLtyJH9-AwAAAEKM9NgOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response)
# print(response.text)
if response.status_code in [200]:
    tok_dict = json.loads(response.text)
    print(tok_dict)
    token_type = tok_dict["token_type"]
    expires_in = tok_dict["expires_in"]
    ext_expires_in = tok_dict["ext_expires_in"]
    access_token = tok_dict["access_token"]
    print("token_type=","Bearer")
    print("access_token=",access_token)
else:
    print(response.text)
