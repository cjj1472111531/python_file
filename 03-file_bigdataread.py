# coding=gbk
# @file:03-file_bigdataread.py
# @data:2021/7/4 21:14
# Editor:clown
f= open('1.txt','r',encoding='utf-8')
while True:
    buf=f.readline()
    if buf:  #if len(buf)>0
        print(buf,end='')
    else:
        break
f.close()