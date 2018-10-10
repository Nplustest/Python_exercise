import re
'''
text = str(input())
def password(text):
	if len(text) < 8:
		return False
	m1 = re.compile(r'[A-Z]+')
	if m1.search(text) == None:
		return False
	m2 = re.compile(r'[a-z]+')
	if m2.search(text) == None:
		return False
	m3 = re.compile(r'\d+')
	if m3.search(text) == None:
		return False
	else:
		return True
print(password(text))
'''
a = str(input("请输入原始字符串:"))
b = str(input("请输入删除需要的字符:"))
def strip(a,b):
	if b is None:
		c = re.compile('^ *| *$')
	else:
		c = re.compile(r'^['+b+']*|['+b+']*$')
	return c.sub('',a)
print(strip(a,b))
