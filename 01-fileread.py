### coding=gbk
# 1.���ļ�
# open111(file, mode='r',  encoding=None, ):
# file �ļ��� str
# mode �򿪷�ʽ r ֻ��  w ֻд  a��append����Ӵ�
# en �ļ������ʽ  GBK UTF-8
# ����ֵ�ļ�����

#��ֻ���ķ�ʽ��1.txt �ļ�  �ļ�����ͱ���
f = open('1.txt', 'r',encoding='utf-8')

# 2.��д�ļ�  �� �ļ�����.read()3
# �ļ�����.read(n) nΪ��ȡ�����ֽڵ�����  ��д  Ĭ�϶�дȫ������
buf = f.read(3)
print(buf)
print("*"*30)
#���Ҳ���㻻�з�  ��˻��з�Ҳ��һ���ֽ�
buf = f.read(3)
print(buf)
# 3.�ر��ļ�  �ļ�.close()   ���ڴ�������ļ�ͬ����Ӳ����
f.close()