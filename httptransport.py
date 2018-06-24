import requests


class HttpEndpoint:

    base_url = 'https://lalala'

    def http_get(self, url: str):
        response = requests.get(self.base_url + url)
        return response

    def http_post(self, url: str):
        response = requests.post(self.base_url + url)
        return response


class Sraka:

    def srakacall(self):
        print('sraka')
