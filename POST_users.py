import requests
import json

url = "https://graph.microsoft.com/v1.0/users"
Bearer = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IkVCR29hdFd3VDZCN2VVbkh4Z2kyczZrTkZrZjN1TEQwS1h1WmJzVWZQRUkiLCJhbGciOiJSUzI1NiIsIng1dCI6Imwzc1EtNTBjQ0g0eEJWWkxIVEd3blNSNzY4MCIsImtpZCI6Imwzc1EtNTBjQ0g0eEJWWkxIVEd3blNSNzY4MCJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC84NGY3ZDI5MC1mYTM1LTQxYTgtYTkwMi1jYTFlOGY0NDdlYjQvIiwiaWF0IjoxNjMzODYzMjg0LCJuYmYiOjE2MzM4NjMyODQsImV4cCI6MTYzMzg2NzE4NCwiYWlvIjoiRTJaZ1lPRE1kWDVqWDJSODUyZlcxZElONWd2NkFBPT0iLCJhcHBfZGlzcGxheW5hbWUiOiJEZW1vR3JhcGhBUEkiLCJhcHBpZCI6IjI2YTdmNmM1LWVkMDEtNDdmYy04NmY1LWZjMjQyZDUwYjdhNCIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzg0ZjdkMjkwLWZhMzUtNDFhOC1hOTAyLWNhMWU4ZjQ0N2ViNC8iLCJpZHR5cCI6ImFwcCIsIm9pZCI6ImZjNDUwZGQxLTAxYmYtNGZjNC04NmEwLTk1Yjg3MDFhNGZjMCIsInJoIjoiMC5BWEVBa05MM2hEWDZxRUdwQXNvZWowUi10TVgycHlZQjdmeEhodlg4SkMxUXQ2UnhBQUEuIiwicm9sZXMiOlsiVXNlckF1dGhlbnRpY2F0aW9uTWV0aG9kLlJlYWQuQWxsIiwiVXNlci5SZWFkV3JpdGUuQWxsIiwiVXNlckF1dGhlbnRpY2F0aW9uTWV0aG9kLlJlYWRXcml0ZS5BbGwiLCJEaXJlY3RvcnkuUmVhZFdyaXRlLkFsbCIsIkRpcmVjdG9yeS5SZWFkLkFsbCIsIlVzZXIuUmVhZC5BbGwiLCJVc2VyLk1hbmFnZUlkZW50aXRpZXMuQWxsIiwiUm9sZU1hbmFnZW1lbnQuUmVhZFdyaXRlLkRpcmVjdG9yeSJdLCJzdWIiOiJmYzQ1MGRkMS0wMWJmLTRmYzQtODZhMC05NWI4NzAxYTRmYzAiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiQVMiLCJ0aWQiOiI4NGY3ZDI5MC1mYTM1LTQxYTgtYTkwMi1jYTFlOGY0NDdlYjQiLCJ1dGkiOiIyVkFrbVRrQlNVV0tIdTh0S3FmRUFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyIwOTk3YTFkMC0wZDFkLTRhY2ItYjQwOC1kNWNhNzMxMjFlOTAiXSwieG1zX3RjZHQiOjE2MzM1MDMyODZ9.fdtUZbzOFoU6Py_Chc-3VlyTfuq8hT-ickJfsdQQZsdqAECspBxE1ODrmomkJcNhz2ImG7D_VWhkaf2kLID4mbZKQgbcE9i_-9Z6OlxgLxDnu2k91m78tXIOEmo_SbVZiwFBQGI-tY49M85zb5hjqbZUTHXg-mUobJI-yq-Tlhq89ZjUEIhJibHFPXl6rlgCbyAYwgW1A1WEKVCC4yCMf4nMnP2Y-uHAbOYr6ut_WYtMQeQvIUwLkFt1K8Kqi43MeJP8FrvhQnWXZh9wl4C3lZbGyuLQTA6iSZP-47VBUKsGXe0jjokdXbYfMjj0f_U-nQpSjRBCi1Uz3QXQn11mbg"


payload = json.dumps({
    "accountEnabled": True,
    "displayName": "papa",
    "mailNickname": "papa",
    "userPrincipalName":"papa@amittiwari8877outlook.onmicrosoft.com",
    # "userPrincipalName": "amittiwari8877outlook.onmicrosoft.com",
    "passwordProfile": {
        "password": "47370646-53bc-6e75-5a9c-c0777a3fea83",
        "forceChangePasswordNextSignIn": False
    }

})
headers = {
  'Authorization': Bearer,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

if response.status_code in [201]:
    print("user created successfully")
else:
    response_dict = json.loads(response.text)
    #print(response_dict)
    message1 = response_dict["error"]["message"]
    print(message1)
