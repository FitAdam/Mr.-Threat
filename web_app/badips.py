import requests
import json

class BadIPs:
    """This class is used to check IPs with BadIPs API"""
    def __init__(self, ipAddress):
        self.ipAddress = ipAddress
        self.url = self.get_url_with_ip()


    def get_url_with_ip(self):
        """Returns url with IP needed for request"""
        url = "https://www.badips.com/get/info/"
        url += self.ipAddress
        return url


    def send_the_request_to_badips(self):
        """This function checks the IP against badips database."""
        response = requests.request("GET", self.url)
        return response


    def get_output(self, new_response):
        """This function using json.loads turns data into a python dictionary."""
        decodedResponse = json.loads(new_response.text)
        # Formatted output
        return decodedResponse


    def check_the_ip_with_badips(self):
        """This function takes user input, checks the IP and returns the answer"""
        response = self.send_the_request_to_badips()
        answer = self.get_output(response)
        return answer

