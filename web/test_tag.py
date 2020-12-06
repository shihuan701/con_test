import json
import time

import requests

from web.tag import Tag


def test_tag_list():
    tag = Tag()
    r = tag.list()

    tag_name = 'shiyi'+ str(time.time())
    r = tag.edit(id='etILlkCwAArWGCRm9_YgQuAjdD5GGmDA',tag_name=tag_name)
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    ## 查询列表判断是否更新成功
    r = tag.list()
    tags = [
            tag for group in r.json()['tag_group'] if group['group_name'] == 'important'
            for tag in group['tag'] if tag['name'] == tag_name
    ]
    assert len(tags) >0