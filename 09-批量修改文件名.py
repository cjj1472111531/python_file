# coding=gbk
# @file:09-批量修改文件名.py
# @data:2021/7/5 16:33
# Editor:clown
import os


# os.remove('file_0.txt')
# os.remove("file_1.txt")

def create_file():
    os.chdir('clown')  # 转到那一个目录下
    for i in range(2, 5):
        file_name = 'file_' + str(i) + '.txt'  # 当前目录下添加
        # file_name='clown/file_'+str(i)+'.txt' #当前目录下添加
        print(file_name)
        f = open(file_name, 'w', encoding='utf-8')
        f.write(input("请输入的内容"))
        f.close()
        # ../是返回上一级目录  切换过去再切换回来 负责任做法
    os.chdir('../')


def modify_filename():  # 自写 在自写列表上修改文件名
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


def modify_filename1():  # 自己输入文件名
    z = ['a', 'b', 'c', 'd', 'e']
    os.chdir('clown')
    buf_list = os.listdir()
    # print(buf_list)
    j = 0
    for i in z:
        # print(i,end=' ')
        # oldfile_name='clown/file_'+str(j)
        newfile_name = input("输入文件名")
        os.rename(buf_list[j], newfile_name)
        j += 1
    os.chdir('../')

def write_filename():  # 自己输入文件名
    os.chdir('clown')#打开当前级目录
    buf_list=os.listdir()
    print(buf_list)
    j=0
    for i in buf_list:
        f=open(i,'w',encoding='utf-8')
        f.write(input("请书写文件内容:"))
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
# create_file()  #批量创建文件
# modify_filename1()  #批量修改文件名
write_filename()     #批量写文件名