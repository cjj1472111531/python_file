# coding=gbk
# @file:08-filecaozuo.py
# @data:2021/7/5 13:10
# Editor:clown
#�ļ�Ŀ¼����������osģ��
import os
#�޸��ļ�����
# os.rename('1.txt','rename.txt')

# ɾ���ļ�
# os.remove('1[����].txt')
# os.remove('������.txt')
# os.remove('text1[����].PNG')

#�����ļ��� mkdir  m k==make
# os.mkdir('clown/tect')
#��ȡ��ǰĿ¼
# print("*"*30)
buf=os.getcwd()
print(buf)
#�ı�Ĭ��Ŀ¼  ���Ǵ���ᵽ�Ǹ��ļ��� ���ǽ������������޸ĵ�Ŀ¼��
#  ch ==change
# os.chdir('')

#��ȡĿ¼�б�  ��д������ Ĭ�ϵ�ǰĿ¼    д���� ����Ŀ��Ŀ¼
buf=os.listdir('clown')
print(buf)
buf=os.listdir()
print(buf)

#ɾ���ļ���  rmdir  r m==remove
# os.rmdir("clown/tect")