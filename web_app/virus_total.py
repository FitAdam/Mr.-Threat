import requests
import json
# key

from keys import virus_total_key

url = "https://www.virustotal.com/api/v3/ip_addresses/79.143.44.122"

def get_querystring(ipAddress, maxAgeInDays):
    """Returns querysting needed for request"""
    querystring = {
    "ip": ip,
    'maxAgeInDays': maxAgeInDays}
    return querystring


def get_headers(virus_total_key):
    """Returns the headers"""
    headers = {
        'x-apikey': virus_total_key,
    }
    return headers

headers = get_headers(virus_total_key)
querystring = {"limit":"10"}

response = requests.request("GET", url, params=querystring, headers=headers)

print(response.text)