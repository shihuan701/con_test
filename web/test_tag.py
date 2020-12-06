import json
import time

import requests


def test_tag_list():
    corpid = 'wweff799876fd1e687'
    corpsecret = 'hDRw6k0Q0lXdfTFsG1Baakf8CzuKuJzdqoo3x-euGnM'
    r = requests.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                     params={'corpid':corpid,'corpsecret':corpsecret})
    assert r.status_code==200
    assert r.json()['errcode'] == 0
    token = r.json()['access_token']
    r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                  params={'access_token':token},
                  )
    print(json.dumps(r.json(),indent=2))
    assert r.status_code==200
    assert r.json()['errcode'] ==0
    tag_name = 'shiyi'+ str(time.time())
    r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                      params={'access_token': token},
                      json ={'id':'etILlkCwAArWGCRm9_YgQuAjdD5GGmDA','name': tag_name})

    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    ## 查询列表判断是否更新成功
    r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                      params={'access_token': token},
                      )
    tags = [
            tag for group in r.json()['tag_group'] if group['group_name'] == 'important'
            for tag in group['tag'] if tag['name'] == tag_name
    ]
    assert len(tags) >0