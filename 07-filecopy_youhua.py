# coding=gbk
# @file:07-filecopy_youhua.py
# @data:2021/7/5 12:18
# Editor:clown
filename = input("�����뱸�ݵ��ļ���")
# ���ļ� ��ȡ��������ݽ��д洢
f = open(filename, 'rb')
buf = f.read()
# print(buf)
f.close()

# ����ԭ�ļ��� �ҵ��ļ���׺���ļ���
# rfind�������ַ������һ�γ��ֵ�λ�ã����û��ƥ�����򷵻� -1��
dian = filename.find('.')
# �ļ���
wenjianming = filename[0:dian]
# ��׺  ���Ϻ�׺����˼�������ļ�����ʲô��ʽ���д�
houzui = filename[dian:len(filename)]
print(wenjianming, houzui)

new_filename = wenjianming + '[����]' + houzui

# д�ļ� д������ ֮��ر����ļ�
f1 = open(new_filename, 'wb')
f1.write(buf)
f1.close()
