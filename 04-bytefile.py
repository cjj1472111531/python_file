# coding=gbk
# @file:04-bytefile.py
# @data:2021/7/5 11:54
# Editor:clown
# �������ļ� mp3 mp4 rmvb avi png jpg
# �������ļ�ֻ���ö����Ʒ�ʽ  rb wb ab  ����ָ������encoding
# ���ܶ�ȡ ������д ����Ҫ����������
f=open('c.txt','wb')
# encode() ת��ɶ���������  decode() ���������
f.write('���'.encode())
# ǰ�棫b  ���������
f.write(b'01001010101')

f.close()

f1=open("c.txt",'rb')
buf=f1.read()
print(buf.decode())
f1.close()