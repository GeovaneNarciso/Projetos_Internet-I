import requests
import json


class RequestApi:
    def __init__(self, url):
        self.url = url

    def get(self):
        return json.loads(requests.get(self.url).content)

    def post(self, payload):
        return json.loads(requests.post(self.url, data=payload).content)

