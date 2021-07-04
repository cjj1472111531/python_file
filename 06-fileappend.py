# coding=gbk
# @file:06-fileappend.py
# @data:2021/7/4 18:34
# Editor:clown
# a 方式打开文件追加内容 在文件末尾写内容
# 文件不存在 会创建
#  无论 a 方式打开  w方式打开   都是使用write函数进行打开
f=open('1.txt','a',encoding='utf-8')

f.write("\nFuck")

f.close()