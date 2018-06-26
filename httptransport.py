import requests
import utils


class Endpoint:

    base_url = ''

    def __init__(self, bid):
        self.base_url = 'https://lalala/' + bid + '/other_stuff'

    def http_get(self, url: str):
            print('calling: ' + self.base_url + url)
            response = requests.get(self.base_url + url)
            return response

    def http_post(self, url: str):
        response = requests.post(self.base_url + url)
        return response

