# -*- coding=utf-8 -*-

lines = (i for i in open('./word.txt', 'r') if '得分' not in i and '分数' not in i)
f = open('write.txt', 'w')
f.writelines(lines)


