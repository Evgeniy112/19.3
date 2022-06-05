import requests


class Moyklass:
    def __init__(self):
        self.base_url = "https://app.moyklass.com/settings/settings/api/api"


    def get_api_key(self, email, password):
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
