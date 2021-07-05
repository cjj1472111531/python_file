# coding=gbk
# @file:08-filecaozuo.py
# @data:2021/7/5 13:10
# Editor:clown
#文件目录操作，导入os模板
import os
#修改文件名字
# os.rename('1.txt','rename.txt')

# 删除文件
# os.remove('1[备份].txt')
# os.remove('！！！.txt')
# os.remove('text1[备份].PNG')

#创建文件夹 mkdir  m k==make
# os.mkdir('clown/tect')
#获取当前目录
# print("*"*30)
buf=os.getcwd()
print(buf)
#改变默认目录  不是代码搬到那个文件中 而是将代码运行在修改的目录中
#  ch ==change
# os.chdir('')

#获取目录列表  不写参数是 默认当前目录    写参数 则是目标目录
buf=os.listdir('clown')
print(buf)
buf=os.listdir()
print(buf)

#删除文件夹  rmdir  r m==remove
# os.rmdir("clown/tect")