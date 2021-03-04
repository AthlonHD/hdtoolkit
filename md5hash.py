# -*- coding=utf-8 -*-
# -*- author=AthlonHD -*-

import hashlib

print('======md5加盐值加密程序======\n')

pwd = input('请输入要加密的内容：\n').encode('utf-8')
print('')
salt = input('请输入加盐的值：\n').encode('utf-8')
print('')

md5_pwd = hashlib.md5(b'%s' % salt)
md5_pwd.update('%s'.encode('utf-8') % pwd)
secret = md5_pwd.hexdigest().upper()


print('=========加 密 结 果=========')
print(secret)




