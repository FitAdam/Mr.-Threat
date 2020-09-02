import requests
import json

def get_url_with_ip(ipAddress):
    """Returns url with IP needed for request"""
    url = "https://www.badips.com/get/info/"
    url += ipAddress
    return url


def send_the_request_to_badips(url):
    """This function checks the IP against badips database."""
    response = requests.request("GET", url)
    return response


def get_output(new_response):
    """This function using json.loads turns data into a python dictionary."""
    decodedResponse = json.loads(new_response.text)
    # Formatted output
    return decodedResponse


def check_the_ip_with_badips(the_ip):
    """This function takes user input, checks the IP and returns the answer"""
    url = get_url_with_ip(the_ip)
    response = send_the_request_to_badips(url)
    answer = get_output(response)
    return answer

test = check_the_ip_with_badips("114.216.105.17")
print(test)