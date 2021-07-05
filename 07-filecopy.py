# coding=gbk
# @file:07-filecopy.py
# @data:2021/7/5 12:06
# Editor:clown
#打开文件 读取文件 保存读取数据
f=open('1.txt','rb')
buf=f.read()
print(buf)
f.close()
#写文件 写新内容 之后关闭新文件
f1=open('copy.txt','wb')
f1.write(buf)
f1.close()
