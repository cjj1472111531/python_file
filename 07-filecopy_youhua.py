# coding=gbk
# @file:07-filecopy_youhua.py
# @data:2021/7/5 12:18
# Editor:clown
filename = input("请输入备份的文件名")
# 读文件 读取里面的数据进行存储
f = open(filename, 'rb')
buf = f.read()
# print(buf)
f.close()

# 根据原文件名 找到文件后缀和文件名
# rfind函数：字符串最后一次出现的位置，如果没有匹配项则返回 -1。
dian = filename.find('.')
# 文件名
wenjianming = filename[0:dian]
# 后缀  加上后缀的意思就是让文件采用什么形式进行打开
houzui = filename[dian:len(filename)]
print(wenjianming, houzui)

new_filename = wenjianming + '[备份]' + houzui

# 写文件 写新内容 之后关闭新文件
f1 = open(new_filename, 'wb')
f1.write(buf)
f1.close()
