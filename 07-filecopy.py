# coding=gbk
# @file:07-filecopy.py
# @data:2021/7/5 12:06
# Editor:clown
#���ļ� ��ȡ�ļ� �����ȡ����
f=open('1.txt','rb')
buf=f.read()
print(buf)
f.close()
#д�ļ� д������ ֮��ر����ļ�
f1=open('copy.txt','wb')
f1.write(buf)
f1.close()
