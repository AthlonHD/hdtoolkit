# -*- coding=utf-8 -*-
import re

with open('base64编码.txt', 'r') as f:
    raw_code = f.read()
processed_code = re.sub(r'data:image/.+?;base64,', '', raw_code)
print(processed_code)

with open('processed_base64编码.txt', 'w') as f:
    f.write(processed_code)