import requests

from web.base_api import BaseApi


class Tag(BaseApi):

    def __init__(self):
        super().__init__()



    def add(self,group_name,tag_name_list,**kwargs):
        json = {
            "group_name": group_name,
            "tag": tag_name_list,
            **kwargs
        }
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            'params': {'access_token': self.token},
            'json':json

        }
        r = self.send(data)
        return r

    def delete_group(self,group_id):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            'params': {'access_token': self.token},
            'json': {'group_id': group_id}

        }
        r = self.send(data)
        return r

    def delete_tag(self, tag_id):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            'params': {'access_token': self.token},
            'json': {'tag_id': tag_id}

        }
        r = self.send(data)
        return r

    def edit(self,id,tag_name):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            'params': {'access_token': self.token},
            'json': {'id':id,'name': tag_name}

        }
        r = self.send(data)
        return r

    def list(self):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            'params': {'access_token': self.token},
            'json': {'tag_id':[]}

        }
        r = self.send(data)
        return r


    def add_before_check(self,group_name,tag_name_list,**kwargs):
        r = self.add(group_name,tag_name_list,**kwargs)
        # 判断group是否存在
        if r.json()['errcode'] == 40071:
            group_id = self.find_id_by_name(group_name)
            if not group_id:
                return False
            # 如果group_name 存在，需要删除group
            self.delete_group(group_id)
            # 删除完后再添加group
            self.add(group_name,tag_name_list,**kwargs)
        #添加完后再次判断是否存在
        result = self.find_id_by_name(group_name)
        if not result:
            print('group_name 没有添加成功')
        return result

    def find_id_by_name(self,group_name):
        for group in self.list().json()['tag_group']:
            if group_name in group['group_name']:
                return group['group_id']
        print('group_name 不存在')
        return ''

    def is_group_id_exit(self,group_id):
        for group in self.list().json()['tag_group']:
            if group_id in group['group_id']:
                return True
        return False

    def delete_and_check_group(self,group_ids,group_name,tag_name_list,):
        deleted_group_id = []
        r = self.delete_group(group_ids)
        if r.json()['errcode'] == 40068:
            for group_id in group_ids:
                # 如果group_id不存在,则添加一个标签并把group_id 存储起来
                if not self.is_group_id_exit(group_id):
                    group_id_tmp = self.add_before_check(group_name,tag_name_list)
                    deleted_group_id.append(group_id_tmp)
                else:
                    deleted_group_id.append(group_id)
            r = self.delete_group(deleted_group_id)
        return False

