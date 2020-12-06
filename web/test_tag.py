import json
import time

import pytest

from web.tag import Tag

class TestTag():

    def setup(self):
        self.tag = Tag()


    @pytest.mark.parametrize('tag_id,tag_name',[
        ['etILlkCwAArWGCRm9_YgQuAjdD5GGmDA','shiyi']
    ])
    def test_tag_list(self,tag_id,tag_name):
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

