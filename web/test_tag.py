import json

import requests


def test_tag_list():
    corpid = 'wweff799876fd1e687'
    corpsecret = 'hDRw6k0Q0lXdfTFsG1Baakf8CzuKuJzdqoo3x-euGnM'
    r = requests.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                     params={'corpid':corpid,'corpsecret':corpsecret})
    print(json.dumps(r.json(), indent=2))
    assert r.status_code==200
    assert r.json()['errcode'] == 0
    token = r.json()['access_token']
    r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                  params={'access_token':token},
                  )

    print(json.dumps(r.json(),indent=2))
    assert r.status_code==200
    assert r.json()['errcode'] ==0

    r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                      params={'access_token': token},
                      json ={'id':'etILlkCwAArWGCRm9_YgQuAjdD5GGmDA','name': 'interesting——new'})

    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0