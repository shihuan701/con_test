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

    def add(self,group_name,tag_name_list,**kwargs):
        json = {
            "group_name": group_name,
            "tag": tag_name_list,
            **kwargs
        }
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                          params={'access_token': self.token},
                          json=json)
        return r

    def delete_group(self,group_id):
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                          params={'access_token': self.token},
                          json={'group_id': group_id})
        return r

    def delete_tag(self, tag_id):
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                          params={'access_token': self.token},
                          json={'tag_id': tag_id})
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


    def add_before_check(self,group_name,tag_name_list,**kwargs):
        r = self.add(group_name,tag_name_list,**kwargs)
        # 判断group是否存在
        if r.json()['errcode'] == 40071:
            group_id = self.find_name_by_id(group_name)
            if not group_id:
                return False
            # 如果group_name 存在，需要删除group
            self.delete_group(group_id)
            # 删除完后再添加group
            self.add(group_name,tag_name_list,**kwargs)
        #添加完后再次判断是否存在
        result = self.find_name_by_id(group_name)
        if not result:
            print('group_name 没有添加成功')
        return result

    def find_name_by_id(self,group_name):
        for group in self.list().json()['tag_group']:
            if group_name in group['group_name']:
                return group['group_id']
        print('group_name 不存在')
        return ''

    def is_group_id_exit(self,group_id):
        for group in self.list().json()['tag_group']:
            if group_id in group['group_id']:
                return True
        print('group_id 不存在')
        return False

    def delete_and_check_group(self,group_ids,group_name,tag_name_list,):
        deleted_group_id = []
        r = self.delete_group(group_ids)
        if r.json()['errcode'] == 40068:
            for group_id in group_ids:
                # 如果group_id不存在,则添加一个标签并把group_id 存储起来
                if not self.is_group_id_exit(group_id):
                    group_id = self.add_before_check(group_name,tag_name_list).json()['tag_group']['group_id']
                    deleted_group_id.append(group_id)
                else:
                    deleted_group_id.append(group_id)
            r = self.delete_group(deleted_group_id)
        print('group_id 不存在')
        return False

