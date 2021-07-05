# coding=gbk
# @file:04-bytefile.py
# @data:2021/7/5 11:54
# Editor:clown
# 二进制文件 mp3 mp4 rmvb avi png jpg
# 二进制文件只能用二进制方式  rb wb ab  不能指定参数encoding
# 不管读取 还是书写 都需要二进制数据
f=open('c.txt','wb')
# encode() 转变成二进制数据  decode() 解码二进制
f.write('你好'.encode())
# 前面＋b  代表二进制
f.write(b'01001010101')

f.close()

f1=open("c.txt",'rb')
buf=f1.read()
print(buf.decode())
f1.close()