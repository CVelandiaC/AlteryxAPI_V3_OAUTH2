from urllib import response
import requests
import json


class ayx_api_v3:
    def __init__(self, key, secret, hostname):

        self.__api_key = key
        self.__api_secret = secret
        self.__host = hostname
        self.__token = ""
    
    def req_auth_token(self):
        url = self.__host + "/webapi/oauth2/token"
        body = {
                'grant_type':'client_credentials',
                'client_id' : self.__api_key,
                'client_secret' : self.__api_secret
            }

        # Request token
        response = requests.request('POST', url, data = body)
        response = json.loads(response.text)
        self.__token = response['access_token']

    def GET_endpoint(self, endpoint, parameters):

        requestUrl = self.__host + endpoint 
        headers = {'Authorization' : 'Bearer ' + self.__token}

        response = requests.request('GET', url = requestUrl, headers = headers, params = parameters)

        response = json.loads(response.text)

        return response

    def POST_endpoint(self, endpoint, parameters):

        requestUrl = self.__host + endpoint 
        headers = {'Authorization' : 'Bearer ' + self.__token}

        response = requests.request('POST', url = requestUrl, headers = headers, params = parameters)

        response = json.loads(response.text)

        return response