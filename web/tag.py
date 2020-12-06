import requests


class Tag():

    def __init__(self):
        self.token = self.getToken()

    def getToken(self):
        corpid = 'wweff799876fd1e687'
        corpsecret = 'hDRw6k0Q0lXdfTFsG1Baakf8CzuKuJzdqoo3x-euGnM'
        r = requests.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={'corpid': corpid, 'corpsecret': corpsecret})
        token = r.json()['access_token']
        return token

    def add(self):
        pass

    def delete(self):
        pass

    def edit(self,id,tag_name):
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                      params={'access_token': self.token},
                      json ={'id':id,'name': tag_name})
        return r

    def list(self):
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                          params={'access_token': self.token},
                          json= {'tag_id':[]})
        return r