import requests

# 导入此库无视"无视证书"引发的错误
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

header = {'token': '抹去',
          'ProfileToken': '抹去',
          'Content-Type': 'application/json' }

data = {"MediaType": "WeChat",
        "SocialCode": "抹去",
        "AddTime": "2021-01-01"}

url = '抹去'


response = requests.post(url=url, params=data, headers=header, verify=False)    # verify设置False无视ssl证书警告

r = response.text

print(r)