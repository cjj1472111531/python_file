# coding=gbk
# @file:01-fileread_line.py
# @data:2021/7/4 20:40
# Editor:clown
f= open('1.txt','r',encoding='utf-8')
# buf=f.readline()  #���ж�ȡ
# print(buf)

print("*"*30)  #�����´ι�������λ���ٽ��ж�ȡ
#f.readlines()   #һ�ζ�ȡ������ ���Ҳ���ȥ
buf=f.readlines()
print(buf)
# strip��������ֻ��ɾ����ͷ
# ���ǽ�β���ַ�������ɾ���м䲿�ֵ��ַ�
# Ĭ��ת���ַ��Ϳո�
buf=[i.strip()for i in buf]
print(buf)

f.close()