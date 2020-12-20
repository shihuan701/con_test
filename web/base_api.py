import json

import requests


class BaseApi():
    def __init__(self):
        self.token = self.getToken()


    def getToken(self):
        corpid = 'wweff799876fd1e687'
        corpsecret = 'hDRw6k0Q0lXdfTFsG1Baakf8CzuKuJzdqoo3x-euGnM'
        data = {
            'method':'get',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'params':{'corpid': corpid, 'corpsecret': corpsecret}

        }
        r = self.send(data)
        token = r.json()['access_token']
        return token

    def send(self,kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(),indent=2))
        return r