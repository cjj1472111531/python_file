# coding=gbk
# @file:09-�����޸��ļ���.py
# @data:2021/7/5 16:33
# Editor:clown
import os


# os.remove('file_0.txt')
# os.remove("file_1.txt")

def create_file():
    os.chdir('clown')  # ת����һ��Ŀ¼��
    for i in range(2, 5):
        file_name = 'file_' + str(i) + '.txt'  # ��ǰĿ¼�����
        # file_name='clown/file_'+str(i)+'.txt' #��ǰĿ¼�����
        print(file_name)
        f = open(file_name, 'w', encoding='utf-8')
        f.write(input("�����������"))
        f.close()
        # ../�Ƿ�����һ��Ŀ¼  �л���ȥ���л����� ����������
    os.chdir('../')


def modify_filename():  # ��д ����д�б����޸��ļ���
    z = ['a', 'b', 'c', 'd', 'e']
    os.chdir('clown')
    buf_list = os.listdir()
    # print(buf_list)
    j = 0
    for i in z:
        # print(i,end=' ')
        # oldfile_name='clown/file_'+str(j)
        newfile_name = 'file_' + i + '.txt'
        os.rename(buf_list[j], newfile_name)
        j += 1
    os.chdir('../')


def modify_filename1():  # �Լ������ļ���
    z = ['a', 'b', 'c', 'd', 'e']
    os.chdir('clown')
    buf_list = os.listdir()
    # print(buf_list)
    j = 0
    for i in z:
        # print(i,end=' ')
        # oldfile_name='clown/file_'+str(j)
        newfile_name = input("�����ļ���")
        os.rename(buf_list[j], newfile_name)
        j += 1
    os.chdir('../')

def write_filename():  # �Լ������ļ���
    os.chdir('clown')#�򿪵�ǰ��Ŀ¼
    buf_list=os.listdir()
    print(buf_list)
    j=0
    for i in buf_list:
        f=open(i,'w',encoding='utf-8')
        f.write(input("����д�ļ�����:"))
        j+=1
        f.close()
    os.chdir('../')

def  mode():
    os.chdir('clown')
    buflist=os.listdir()
    for   file in buflist:
        num=len('py43_')
        new_file=file[num:]
        os.rename(file,new_file)
    os.chdir('../')
# create_file()  #���������ļ�
# modify_filename1()  #�����޸��ļ���
write_filename()     #����д�ļ���