import requests
import os 

# Replace these with your actual values
# api_token = os.getenv('API_TOKEN')
# zone_id = os.getenv('ZONE_ID')
api_token = "#"
zone_id = "#"

# Cloudflare API endpoint
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

# Headers for the API request
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

# Parameters to list NS records
params = {
    "type": "NS"
}

# Make the API request to list NS records
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    records = response.json()['result']
    for record in records:
        # Extract the record ID
        record_id = record['id']
        # Construct the delete URL
        delete_url = f"{url}/{record_id}"
        # Make the API request to delete the NS record
        delete_response = requests.delete(delete_url, headers=headers)
        if delete_response.status_code == 200:
            print(f"Successfully deleted NS record with ID: {record_id}")
        else:
            print(f"Failed to delete NS record with ID: {record_id}")
else:
    print("Failed to list NS records.")
