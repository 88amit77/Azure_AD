import requests as rq
import json

url = "https://graph.microsoft.com/v1.0/users "

payload = json.dumps({
  "accountEnabled": True,
  "displayName": "displayName-value",
  "mailNickname": "mailNickname-value",
  "userPrincipalName": "upn-value@tenant-value.onmicrosoft.com",
  "passwordProfile": {
    "forceChangePasswordNextSignIn": True,
    "password": "password-value"
  }
})
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI4MTY3NTk2LCJqdGkiOiIwNWFiNzNhNWU5ZDE0NGEwOGYyMzI5NjI4MDJlZWM0MSIsInVzZXJfaWQiOjEwMDN9.83uEHRD2X_le-HB_AU8ysmp1t8_ZDRT2M5XR6U-lHRU',
  'Content-Type': 'application/json'
}

# response = requests.request("POST", url, headers=headers, data=payload)
response = rq.request("POST", url, headers=headers, data=payload)


print(response)
