# coding=gbk
# @file:02-filewrite.py
# @data:2021/7/4 18:33
# Editor:clown
f = open('1.txt', 'w')
f.write("!!!!!!!!")

# 3.�ر��ļ�  �ļ�.close()   ���ڴ�������ļ�ͬ����Ӳ����
f.close()
# window gbk      pycharm ˫����Ĭ�� utf-8 ��˻��������
# ���� ��ν����ĺ��ֱ�Ϊ������  ��ν������Ʊ�Ϊ����
f = open('1.txt', 'w',encoding='utf-8')
f.write("##@@@@@@@####\n")
f.write("��������")
f.close()