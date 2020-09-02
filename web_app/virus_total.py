import requests
import json

# key
from .keys import virus_total_key



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

def format_dict(answer):
    return answer['data']['attributes']['last_analysis_results']

def check_the_ip_with_vt(the_ip):
    """This function takes user input, checks the IP and returns the answer"""
    headers = get_headers(virus_total_key)
    url = get_url_with_ip(the_ip)
    response = requests.request("GET", url, headers=headers)
    answer = get_output(response)
    answer = format_dict(answer)
    return answer



###curl --request GET \
 # --header 'x-apikey: <your API key>' \
  #--url https://www.virustotal.com/api/v3/ip_addresses/{id}/votes  

def get_url_for_votes(ipAddress):
    """Returns url with IP needed for request"""
    url = f'https://www.virustotal.com/api/v3/ip_addresses/'
    url += ipAddress
    url += '/votes'
    return url

def check_the_votes_with_vt(the_ip):
    """This function takes user input, checks the IP and returns the votes"""
    headers = get_headers(virus_total_key)
    url = get_url_with_ip(the_ip)
    response = requests.request("GET", url, headers=headers)
    answer = get_output(response)
    answer = answer['data']['attributes']
    return answer


test = check_the_votes_with_vt('118.100.116.155')
print(test)
"""
checked_dict = checked_dict['data']['attributes']['last_analysis_results']

for key, value in checked_dict.items():
    print(key)
    print(value)
    
"""
