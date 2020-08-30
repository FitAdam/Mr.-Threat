import requests
import json

# keys
from keys import abuseipdb_key


# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

def get_querystring(ipAddress, maxAgeInDays):
    """Returns querysting needed for request"""
    querystring = {
    'ipAddress': ipAddress,
    'maxAgeInDays': maxAgeInDays}
    return querystring

querystring = get_querystring('36.67.32.45', '7')

def get_headers(abuseipdb_key):
    """Returns the headers"""
    headers = {
        'Accept': 'application/json',
        'Key': abuseipdb_key
    }
    return headers

headers = get_headers(abuseipdb_key)

def get_response():
    """This function send the request and returns it as variable"""
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    return response

response = get_response()

def get_output():
    """This function decodes and returns whole answer."""
    # Formatted output
    decodedResponse = json.loads(response.text)
    return json.dumps(decodedResponse, sort_keys=True, indent=4)

print(get_output())