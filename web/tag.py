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

    def add(self,group_id,group_name,order,tag_name,tag_order):
        json = {
            "group_id": group_id,
            "group_name": group_name,
            "order": order,
            "tag": [{
                    "name": tag_name,
                    "order": tag_order
                }
            ]
        }
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                          params={'access_token': self.token},
                          json=json)
        return r

    def delete(self,group_id,tag_id):
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                          params={'access_token': self.token},
                          json={'group_id': group_id, 'tag_id': tag_id})
        return r

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