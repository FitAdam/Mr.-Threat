import requests
import json
# key

from keys import virus_total_key



def get_url_with_ip(ipAddress):
    """Returns url with IP needed for request"""
    url = "https://www.virustotal.com/api/v3/ip_addresses/"
    url += ipAddress
    return url


def get_headers(virus_total_key):
    """Returns the headers"""
    headers = {
        'x-apikey': virus_total_key,
    }
    return headers


headers = get_headers(virus_total_key)
'querystring = {"limit":"1"}
url = get_url_with_ip('23.90.145.44')
response = requests.request("GET", url, headers=headers)

print(response.text)