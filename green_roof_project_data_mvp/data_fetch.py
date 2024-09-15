import requests
import requests
import json

# Client ID and client secret
client_id = 'sh-302cc5ff-9d90-44c7-94ef-80133902ac25'
client_secret = 'JQDVTybdMgb3KB5cbzyx2EEO0ko37YBy'

# Open Data Space OAuth2 token endpoint
auth_url = 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token'

# Set headers for the POST request
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Payload for client_credentials grant type
payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}

# Make the POST request to get the token
response = requests.post(auth_url, data=payload, headers=headers)

# Check if authentication was successful
if response.status_code == 200:
    # Extract the access token from the response
    access_token = response.json().get('access_token')
    print(f"Access Token: {access_token}")
else:
    # Print error if authentication fails
    print(f"Authentication failed with status code {response.status_code}")
    print(response.text)


access_token = response.json().get('access_token')  # Replace this with the actual token

#API endpoint for data retrieval (Sentinel-3 SLSTR data)
api_url = "https://openeo.dataspace.copernicus.eu/"


headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Define the payload with the bounding box for Rhodes Island
payload = {
    "input": {
        "bounds": {
            "bbox": [27.7, 35.8, 28.4, 36.5]  # Bounding box for Rhodes Island
        },
        "data": [
            {
                "type": "S3SLSTR",
                "dataFilter": {
                    "timeRange": {
                        "from": "2023-09-01T00:00:00Z",  # Start date
                        "to": "2023-09-10T23:59:59Z"  # End date
                    }
                }
            }
        ]
    },
    "output": {
        "width": 512,
        "height": 512,
        "responses": [
            {
                "identifier": "default",
                "format": {
                    "type": "image/jpeg"  # Requesting an image output
                }
            }
        ]
    }
}

#POST request to retrieve data
response = requests.post(api_url, json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    with open('temperature_data_rhodes.jpg', 'wb') as f:
        f.write(response.content)
    print("Temperature data for Rhodes Island has been saved as 'temperature_data_rhodes.jpg'.")
else:
    print(f"Error: {response.status_code}")
    print(response.json())
