'''
#字典数据类型
birthdays = {'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 4'}

while True:
	print('Enter a name:')
	name = input()
	if name == '':
		break
	elif name in birthdays:
		print(birthdays[name] +' is the birthdays of '+ name)
	else:
		print('I do not have birthdays information for '+name)
		print('What is thier birthdays?')
		bday = input()
		birthdays[name] = bday
		print('birthdays database updated.')

#keys()、values()、items()方法对应字典中的键、值和键-值对
spam = {'color':'red','age':'24'}
for v in spam.values():
	print(v)
for k in spam.keys():
	print(k)
for i in spam.items():
	print(i)
list(spam.values())
print(list)
for k,v in spam.items():
	print(k)
	print(v)

#setdefault()方法该键不存在时要设置的值。如果该键确实存在，方法就会返回键的值
spam = {'name':'Hou','age':24}
spam.setdefault('color','black')
print(spam)
print(spam.setdefault('color','white'))
	'''
#setdefault()可以计算每个字符出现的次数
message = 'It was a bright cold day in April,and the clocks were striking thirteen.'
count = {}
for char in message:
	count.setdefault(char,0)
	count[char] = count[char]+1
	
print(count)
