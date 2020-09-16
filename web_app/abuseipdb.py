import requests
import json

# key
import os

class AbuseIPDB:
    """This is the class to work with AbuseIPDB API"""
    def __init__(self, ipAddress, maxAgeInDays):
        # Defining the api-endpoint
        self.url_check = 'https://api.abuseipdb.com/api/v2/check'
        # The API key
        self.abuseipdb_key = os.getenv("abuseipdb_key")
        self.ipAddress = ipAddress
        self.maxAgeInDays = maxAgeInDays
        self.querystring = self.get_querystring()
        self.headers = self.get_headers()


    def get_querystring(self):
        """Returns querysting needed for request"""
        querystring = {
        'ipAddress': self.ipAddress,
        'maxAgeInDays': self.maxAgeInDays}
        return querystring


    def get_headers(self):
        """Returns the headers"""
        headers = {
            'Accept': 'application/json',
            'Key': self.abuseipdb_key
        }
        return headers


    def get_response(self):
        """This function send the request and returns it as variable"""
        response = requests.request(method='GET', url= self.url_check, headers=self.headers, params=self.querystring)

        return response



    def get_output(self, new_response):
        """This function using json.loads turns data into a python dictionary."""
        decodedResponse = json.loads(new_response.text)
        # Formatted output
        return decodedResponse



    def check_the_ip_with_abuse(self):
        """This function takes user input, checks the IP and returns the answer"""
        response = self.get_response()
        answer = self.get_output(response)
        answer = answer['data']
        return answer


    def get_the_isp(self, decodedResponse):
        return decodedResponse['data']['isp']



