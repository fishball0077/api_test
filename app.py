import requests
import json
from msal import ConfidentialClientApplication

# Configuration
config = json.load(open('config.json'))

# MSAL Authentication
app = ConfidentialClientApplication(
    config["client_id"],
    authority=config["authority"],
    client_credential=config["client_secret"],
)

# Acquire Token
token_response = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

if "access_token" in token_response:
    access_token = token_response["access_token"]
    print("Access token acquired.")

    # Make a Microsoft Graph API request
    url = "https://graph.microsoft.com/v1.0/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)

    print(f"Response: {response.status_code}")
    print(response.json())
else:
    print("Failed to acquire token:", token_response.get("error_description"))
