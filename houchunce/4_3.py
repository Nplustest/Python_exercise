'''
spam = 42
spam += 1
print(spam)
bacon = ['hi']
bacon *= 3
print(bacon)

#index()方法查询列表中的值
spam = ['a','b','c']
print(spam.index('c'))

#append()方法添加参数到列表的末尾
spam = ['a','b','c']
spam.append('d')
print(spam)

#insert()方法插入参数到列表指定位置
spam = ['a','b','c']
spam.insert(1,'A')
print(spam)

#remove()方法删除列表中的参数，同时存在多个参数只删除第一个
spam = ['a','b','c']
spam.remove('b')
print(spam)

#sort()方法对列表的参数进行排序
spam = ['c','d','a','b']
spam.sort()
print(spam)#正序
spam.sort(reverse=True)#倒序
print(spam)

import random
messages = ['Tt is certain',
	'It is decidedly so',
	'Yes definitely',
	'Reply hazy tru again',
	'Ask again later',
	'Concentrate and ask again',
	'My reply is no',
	'Outlook not so good',
	'Very doubtful']
print(messages[random.randint(0,len(messages)-1)])

tuple(['a','b','c'])#改变列表为元祖
list(('a','b','c'))#改变元祖为列表
list('abc')

#列表赋值给一个变量等于将列表引用
spam = ['1','2','3','4','5']
chesse = spam
chesse[1] = 'a'
print(spam)
print(chesse)

def eggs(someParameter):
	someParameter.append('Hello')

spam = [1.2,3,4]
eggs(spam)#向聊表spam中增加参数
print(spam)
'''
#copy.copy()函数复制列表中的可变值，也可以teepcopy()函数，复制整个列表
import copy
spam = [1,2,3,4,5,6]
chesse = copy.copy(spam)
chesse[1] = 'b'
print(chesse)
print(spam)
