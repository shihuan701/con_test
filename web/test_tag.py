import json
import time

import pytest

from web.tag import Tag

class TestTag():

    def setup(self):
        self.tag = Tag()


    @pytest.mark.parametrize('tag_id,tag_name',[
        ['etILlkCwAArWGCRm9_YgQuAjdD5GGmDA','shiyi'],
        ['etILlkCwAArWGCRm9_YgQuAjdD5GGmDA', '十一'],
        ['etILlkCwAArWGCRm9_YgQuAjdD5GGmDA', '😊']
    ])
    def test_tag_edit(self,tag_id,tag_name):
        tag_name = tag_name+ str(time.time())
        r = self.tag.edit(id=tag_id,tag_name=tag_name)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        ## 查询列表判断是否更新成功
        r = self.tag.list()
        tags = [
                tag for group in r.json()['tag_group'] if group['group_name'] == 'important'
                for tag in group['tag'] if tag['name'] == tag_name
        ]
        assert len(tags) >0

    @pytest.mark.parametrize('group_name,tag_name', [
        [ 'show',['lisi','zhangsan']],
    ])
    def test_tag_add(self,group_name,tag_name):
        r = self.tag.add(group_name,tag_name)
        r = self.tag.list()
        tags = [
            tag for group in r.json()['tag_group'] if group['group_name'] == 'show'
            for tag in group['tag'] if tag['name'] == tag_name[0]
        ]
        assert len(tags) > 0

    def test_tag_list(self):
        r = self.tag.list()
        print(json.dumps(r.json(),indent=2))

    def test_tag_delete(self):
        tag_id = ['etILlkCwAArWGCRm9_YgQuAjdD5GGmDA']
        r = self.tag.delete_tag(tag_id)
        r = self.tag.list()

    def test_group_delete(self):
        group_id = 'etILlkCwAApjzOR5Kw537iJzLPuea1fA'
        r = self.tag.delete_group(group_id)
        r = self.tag.list()
        json.dumps(r.json(),indent=2)




