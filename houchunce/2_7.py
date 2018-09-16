'''
#if,else语句
if name == 'Houchunce':
	print('Hello')
if	password == ‘chunce’:
	print('Access granted.')
else:
	print('Wrong password.')
	'''
	
'''	
#elif语句
if name == 'Chunce':
	print('你好，菜鸟。')
elif age < 20:
	print('小菜鸟')
elif age > 20：
	print('大菜鸟')
else:
	print('老菜鸟')
	'''
	
'''
#while循环
spam = 0
while spam < 6:
	print('Hello,Hou')
	spam = spam + 1
'''

'''
#while循环
name = ''
while name != 'Chunce':
	print('Please type yout name.')
	name = input()
print('OK')
'''

'''
#break语句跳出循环
#name = ''
while True:
	print('Plesse type your name.')
	name = input()
	if name == 'Chunce':
		break
print('OK')	
'''

'''
#continue语句
while True:
	print('Who are you?')
	name = input()
	if name != 'Chunce':
		continue
	print('Hello,Chunce. What is the password?')
	password = input()
	if password == 'chunce':
		break
print('Access granted.')
'''

'''
#for循环的range()函数,固定执行次数
print('My name is')
for i in range(5):
	print('Hou Five Times ('+ str(i) +')')
	'''

'''
#计算1-100的和	
total = 0 
for num in range(101):
	total = total + num
print(total)
'''

#range的用法
for i in range(5,-1,-1)