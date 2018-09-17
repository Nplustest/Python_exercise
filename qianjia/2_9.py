'''
print('1: '+'True==2')
print('2'+':')
print(2==2)
print('3'+':')
print(24==24.00)
print('4'+':')
print(True and True)
print('5'+':')
print(True and False)
print('6'+':')
print(True or False)

print('7'+':')
print((4<5) and (10<5))

'''

#if
#print('请输入姓名'+':')
#name=input()
#print(name)
'''
if name=='Alice':
    print('Hello Alice!')
elif name=='Peter':
    print('Hello Peter!')
elif name=='El':
    print('Hello El!')
else:
    print('Who are you?')
'''

#while
'''
spam=0
while spam<5:
    print('Hello World!')
    print(spam)
    spam=spam+1
    print(str(spam)+'+ha')
'''

#while
'''
name=''
while name!='Hawaii':
    print('Please type your name.')
    name=input()
print('Thank you '+name+'!')
'''

#break
'''
while True:
    print('Please type your name.')
    name=input()
    if name=='Hawaii':
        break
print('Thank you '+name+'!')
'''

'''
#continue
while True:
    print('Who are you?')
    name=input()
    if name != 'Hawaii':
        continue
    print('Welcome,'+name+'. What\'s your password?')
    psd=input()
    if psd=='abcd':
        break
print('Thank you!')
'''

#for循环 和  range()函数
'''
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

for i in range(3):
    print(str(i))
'''

#计算1到10之和
'''
total=0
for num in range(11):
    #print(total)
    total=total + num
    print('num为'+str(num))
print(total)
'''

#使用两种方法循环打印：for，while
'''
for i in range(5):
    print('My name is Hawaii '+str(i))

print('---------------------')

i=0
while i<5:
    print('My name is Hawaii '+str(i))
    i+=1
'''

'''
for i in range(2,10,2):
    print(i)
'''

'''
import random
for i in range(5):
    print(random.randint(1,10))
'''

#sys.exit()

import sys
while True:
    print('请输入退出exit')
    res=input()
    if res == 'exit':
        sys.exit()
    print('你已经选择了'+res+'哦~')
