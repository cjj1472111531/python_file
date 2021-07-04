# coding=gbk
# @file:02-filewrite.py
# @data:2021/7/4 18:33
# Editor:clown
f = open('1.txt', 'w')
f.write("!!!!!!!!")

# 3.关闭文件  文件.close()   将内存的三大文件同步到硬盘中
f.close()
# window gbk      pycharm 双击打开默认 utf-8 因此会出现乱码
# 编码 如何将中文汉字变为二进制  如何将二进制变为汉字
f = open('1.txt', 'w',encoding='utf-8')
f.write("##@@@@@@@####\n")
f.write("！！！！")
f.close()