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

def get_output(new_response):
    """This function using json.loads turns data into a python dictionary."""
    decodedResponse = json.loads(new_response.text)
    # Formatted output
    return decodedResponse

def check_the_ip(the_ip):
    """This function takes user input, checks the IP and returns the answer"""
    headers = get_headers(virus_total_key)
    url = get_url_with_ip(the_ip)
    response = requests.request("GET", url, headers=headers)
    answer = get_output(response)
    return answer


checked_dict = check_the_ip('185.176.27.46')
checked_dict = checked_dict['data']['attributes']

for value, key in checked_dict.items():
    print(key)
    
