# try:
# 	f=open('decode_in_1001','r')
# 	print(f.read())
# finally:
# 	if f:
# 		f.close()

#with语句自动调用close()方法
with open('decode_in_1001','r') as f:
#	print(f.read())
	for line in f.readlines():
		print(line.strip(),'\n') #把末尾的‘\n’删掉

#还可以读取二进制文件，比如图片
# f=open('psbMQHSGFY3.jpg','rb')
# f.readline()

#写文件
with open('write_file.txt','w') as f:
	f.write('Hello,world!')