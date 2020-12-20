import json
import time

import pytest

from web.tag import Tag

class TestTag():

    def setup(self):
        self.tag = Tag()


    @pytest.mark.parametrize('tag_id,tag_name',[
        ['etILlkCwAAFk1Ga_Cd9RKCp6gczg9jlA','shiyi'],
        ['etILlkCwAAFk1Ga_Cd9RKCp6gczg9jlA', '😊'],
        ['etILlkCwAAFk1Ga_Cd9RKCp6gczg9jlA', u'十一']
    ])
    def test_tag_edit(self,tag_id,tag_name):
        tag_name = tag_name+ str(time.time())
        r = self.tag.edit(id=tag_id,tag_name=tag_name)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        ## 查询列表判断是否更新成功
        r = self.tag.list()
        tags = [
                tag for group in r.json()['tag_group'] if group['group_name'] == 'show'
                for tag in group['tag'] if tag['name'] == tag_name
        ]
        assert len(tags) >0

    @pytest.mark.parametrize('group_name,tag_name_list', [
        [ 'show1',[{'name':'lisi'},{'name':'zhangsan'}]],
    ])
    def test_tag_add(self,group_name,tag_name_list):
        r = self.tag.add(group_name,tag_name_list)
        r = self.tag.list()
        tags = [
            tag for group in r.json()['tag_group'] if group['group_name'] == 'show'
            for tag in group['tag'] if tag['name'] == tag_name_list[0]['name']
        ]
        assert len(tags) > 0

    @pytest.mark.parametrize('group_name,tag_name_list', [
        ['show2', [{'name': 'lisi'}, {'name': 'zhangsan'}]],
    ])
    def test_add_before_check(self, group_name, tag_name_list):
        result = self.tag.add_before_check(group_name, tag_name_list)
        r = self.tag.list()
        group = [
            group for group in r.json()['tag_group'] if group['group_name'] == group_name
        ]
        assert len(group) > 0


    def test_tag_list(self):
        r = self.tag.list()
        print(json.dumps(r.json(),indent=2))

    def test_tag_delete(self):
        tag_id = ['etILlkCwAArWGCRm9_YgQuAjdD5GGmDA']
        r = self.tag.delete_tag(tag_id)
        r = self.tag.list()

    def test_group_delete(self):
        group_id = ['etILlkCwAApjzOR5Kw537iJzLPuea1fA']
        r = self.tag.delete_group(group_id)
        r = self.tag.list()
        json.dumps(r.json(),indent=2)

    def test_delete_and_check_group(self):
        r = self.tag.delete_and_check_group('etILlkCwAAOmN0hSIt88WTVHqfdkohqg','show2',[{'name': 'lisi'}, {'name': 'zhangsan'}])




