import re

if __name__=='__main__':
	# re.match(r'^\d{3}\-\d{3,8}$','010-12345')
	# re.match(r'^\d{3}\-\d{3,8}$','010 12345')
	print('working')

	test='ABC-001'
	if re.match(r'[a-zA-Z\_]+\-[0-9a-zA-Z\_]*',test):
		print('ok')
	else:
		print('failed')


'''切分字符串'''
	# 'a b   c'.split('')
	#str=re.split(r'\s+','a b  c')
	# str=re.split(r'[\s\,]+','a,b,  c d')
	# str1=re.split(r'[\s\,\;]+','a,b;;  c d')

	# print(str1)

'''分组'''	
m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

'''IndentationError: unexpected indent=>tab和空格没对齐'''

t='19:05:30'
n=re.match(r'^(0[0-9]|1[0-9]|2[0-3])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(n.group(1))

'''贪婪匹配'''
print(re.match(r'^(\d+)(0*)$','102300').groups())

'''加个？变成非贪婪匹配'''
print(re.match(r'^(\d+?)(0*)$','102300').groups())

'''预编译正则表达式，重复使用时就可以不用编译了'''
re.telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re.telephone.match('010-12345').groups())
print(re.telephone.match('010-8086').groups())


