import requests
import json

# keys
from . keys import abuseipdb_key


# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

def get_querystring(ipAddress, maxAgeInDays):
    """Returns querysting needed for request"""
    querystring = {
    'ipAddress': ipAddress,
    'maxAgeInDays': maxAgeInDays}
    return querystring


def get_headers(abuseipdb_key):
    """Returns the headers"""
    headers = {
        'Accept': 'application/json',
        'Key': abuseipdb_key
    }
    return headers


def get_response(new_headers, new_querystring):
    """This function send the request and returns it as variable"""
    response = requests.request(method='GET', url=url, headers=new_headers, params=new_querystring)

    return response



def get_output(new_response):
    """This function using json.loads turns data into a python dictionary."""
    decodedResponse = json.loads(new_response.text)
    # Formatted output
    return decodedResponse



def check_the_ip(suspect_ip):
    """This function takes user input, checks the IP and returns the answer"""
    querystring = get_querystring( suspect_ip, '7')
    headers = get_headers(abuseipdb_key)
    response = get_response(headers, querystring)
    answer = get_output(response)
    return answer


def get_the_isp(decodedResponse):
    return decodedResponse['data']['isp']

