# coding=gbk
# @file:03-buchong.py
# @data:2021/7/5 12:00
# Editor:clown
# coding=gbk
# @file:06-buchong.py
# @data:2021/7/4 21:20
# Editor:clown
f=open('b.txt','r',encoding='utf-8')
while True:
    buf=f.read(5)
    if len(buf)>0:
        print(buf,end='')
    else:
        break