
import requests
import json
import os
# key
#from .keys import virus_total_key

class VirusTotal:
    """This is the class to work with VirusTotal API"""
    def __init__(self, ipAddress):
        self.ipAddress = ipAddress
        self.virus_total_key = os.getenv("virus_total_key")
        self.url = self.get_url_with_ip()
        self.headers = self.get_headers()
        self.response = self.make_request_to_vt()

    def get_url_with_ip(self):
        """Returns url with IP needed for request"""
        url = "https://www.virustotal.com/api/v3/ip_addresses/"
        url += self.ipAddress
        return url

    def get_headers(self):
        """Returns the headers"""
        headers = {
            'x-apikey': self.virus_total_key,
        }
        return headers

    def get_output(self, new_response):
        """This function using json.loads turns data into a python dictionary."""
        decodedResponse = json.loads(new_response.text)
        # Formatted output
        return decodedResponse

    def format_dict(self, answer):
        return answer['data']['attributes']['last_analysis_results']

    def make_request_to_vt(self):
        """Makes a request to virus total"""
        response = requests.request("GET", self.url, headers=self.headers)
        return response

    def check_the_ip_with_vt(self):
        """This function takes user input, checks the IP and returns the answer"""
        answer = self.get_output(self.response)
        answer = self.format_dict(answer)
        return answer

    def check_the_votes_with_vt(self):
        """This function checks IP and returns the votes"""
        answer = self.get_output(self.response)
        return answer['data']['attributes']
        
