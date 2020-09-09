import requests
import json
import base64

from keys import phish_tank_key

class PhishTank:
    """This class is used to check URI with Phish Tank API"""
    def __init__(self, URI):
        self.URI = URI
        self.url = "http://checkurl.phishtank.com/checkurl/"
        self.request_url = self.get_url_with_ip()
        self.headers = self.get_headers()


    def get_url_with_ip(self):
        """Returns url with added URI for request"""
        url = "http://checkurl.phishtank.com/checkurl/"
        new_check_bytes = self.URI.encode()
        base64_bytes = base64.b64encode(new_check_bytes)
        base64_new_check = base64_bytes.decode('ascii')
        request_url = url + base64_new_check
        return request_url

    def get_headers(self):
        """Returns the headers"""
        headers = {
            'format': 'json',
            'app_key': phish_tank_key,
        }
        return headers

    def send_the_request_to_phish_tank(self):
        """This function sends a request."""
        response = requests.request("POST", url=self.request_url, headers=self.headers)
        return response


    def get_output(self, new_response):
        """This function using json.loads turns data into a python dictionary."""
        decodedResponse = json.loads(new_response.text)
        # Formatted output
        return decodedResponse


    def check_the_URI_with_pt(self):
        """This function checks the URI and returns the answer"""
        response = self.send_the_request_to_phish_tank()
       # answer = self.get_output(response)
        return response #answer

