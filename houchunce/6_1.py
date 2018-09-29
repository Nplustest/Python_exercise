'''
#\转义字符
print('Hello there!\nHow are you?\nI\'m doing fine.')
#r标识原始字符串
print(r'That is Carol\'s cat.')
#多行字符串,###多行注释
###1
2
3###
print(''''''这是第一行
		这是第二行，什么字都没有
		这是第三行'''''')'''
'''
#lower()方法，字符串变为小写，upper()变为大写
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
	print('I feel great too.')
else:
	print('I hope the rest of your fay is good.')

while True:
	print('Enter your age:')
	age = input()
	if age.isdecimal():
		break
	print('Please enter a number for your age.')
	
while True:
	print('Select a new password (letters and numbers only):')
	password = input()
	if password.isalnum():
		break
	print('Passwords can only have letters and numbers.')
	
#startswith(),endswith()方法
'hello word'.startswith('hello')
'hello word'.endswith('word')
'adc123'.startswith('adbcd')
#join(),split()方法
','.join(['cats','rats','bats'])
' '.join(['My','name','is','Tom'])
'My name is Tom'.split()
'my,name,is,Tom'.split(',')
#rjust(),ljust(),center()方法
'hello'.rjust(10)
'hello'.rjust(10,'*')
'hello'.ljust(10,'*')
'hello'.center(11,'*')

def printPicnic(itemsDict,leftWidth,rightWidth):
	print('PICNIC ITEMS'.center(leftWidth + rightWidth,'-'))
	for k,v in itemsDict.items():
		print(k.ljust(leftWidth,'-')+str(v).rjust(rightWidth,'-'))
picnicItems = {'sandwiches':4,'apples':12,'cups':4,'cookies':8000}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)
'''
#strip()方法，删除首尾制定字符,字符顺序不重要
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
