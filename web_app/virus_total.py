
import requests
import json

# key
from .keys import virus_total_key

class VirusTotal:
    """This is the class to work with VirusTotal API"""
    def __init__(self, ipAddress):
        self.ipAddress = ipAddress
        self.virus_total_key = virus_total_key
        self.url = self.get_url_with_ip()
        self.url_votes = self.get_url_for_votes()
        self.headers = self.get_headers()

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




    def check_the_ip_with_vt(self):
        """This function takes user input, checks the IP and returns the answer"""
        response = requests.request("GET", self.url, headers=self.headers)
        answer = self.get_output(response)
        answer = self.format_dict(answer)
        return answer


    def get_url_for_votes(self):
        """Returns url with IP needed for request"""
        url_votes = "https://www.virustotal.com/api/v3/ip_addresses/"
        url_votes += "77.81.166.81"
        url_votes += "/votes"
        return url_votes

    def check_the_votes_with_vt(self):
        """This function checks IP and returns the votes"""
        response = requests.request("GET", self.url, headers=self.headers)
        answer = self.get_output(response)
        return answer['data']['attributes']
        



#fresh_test = VirusTotal('45.142.120.137')

#print(fresh_test.check_the_ip_with_vt())

#bood_test = VirusTotal('77.81.166.81')
#print(fresh_test.check_the_votes_with_vt())