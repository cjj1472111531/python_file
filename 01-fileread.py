### coding=gbk
# 1.打开文件
# open111(file, mode='r',  encoding=None, ):
# file 文件名 str
# mode 打开方式 r 只读  w 只写  a（append）添加打开
# en 文件编码格式  GBK UTF-8
# 返回值文件对象

#以只读的方式打开1.txt 文件  文件不存就报错
f = open('1.txt', 'r',encoding='utf-8')

# 2.读写文件  读 文件对象.read()3
# 文件对象.read(n) n为读取多少字节的内容  不写  默认读写全部内容
buf = f.read(3)
print(buf)
print("*"*30)
#光标也会算换行符  因此换行符也算一个字节
buf = f.read(3)
print(buf)
# 3.关闭文件  文件.close()   将内存的三大文件同步到硬盘中
f.close()