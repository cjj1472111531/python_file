# coding=gbk
# @file:01-fileread_line.py
# @data:2021/7/4 20:40
# Editor:clown
f= open('1.txt','r',encoding='utf-8')
# buf=f.readline()  #按行读取
# print(buf)

print("*"*30)  #进行下次光标结束的位置再进行读取
#f.readlines()   #一次读取所有行 光标也算进去
buf=f.readlines()
print(buf)
# strip函数方法只能删除开头
# 或是结尾的字符，不能删除中间部分的字符
# 默认转义字符和空格。
buf=[i.strip()for i in buf]
print(buf)

f.close()