import requests

# 导入此库无视"无视证书"引发的错误
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

header = {'token': '3e0ac8d2-190c-4047-9582-066eed9b3066',
          'ProfileToken': 'F2BCE9044A474C39BF1F8466708C2D9E',
          'Content-Type': 'application/json' }

data = {"MediaType": "WeChat",
        "SocialCode": "GH1NB1EDD14HJK5NFG",
        "AddTime": "2021-01-01"}

url = 'https://crmmemberuat.dc.capitaland.com/api/Profile/BindSocial'


response = requests.post(url=url, params=data, headers=header, verify=False)    # verify设置False无视ssl证书警告

r = response.text

print(r)