spam='Hello'
spam+=' World'
print(spam)

a=['apple']
a*=3
print(a)

name=['Alice','Peter','Orz','Hawaii']
print(name.index('Hawaii'))

spam=[1,2]
spam.append(10)
print(spam)
spam.insert(0,77)
print(spam)
spam.remove(1)
print(spam)

spam=['app','mon','lal','mon']
print(spam.index('mon'))  #只显示第一次出现的下标 1
spam.remove('mon')
print(spam)  #只删除第一次出现的'mon'

#排序
spam=['a','d','b','c']
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

spam=['a','Z','b','z','C']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)

spam=[5,4,9]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

import random
messages=['a','b','c','d']
print(messages[random.randint(0,len(messages)-1)])
#print(random.randint(1,3))
a='Hello'
for i in range(5):
    print(a)

for i in range(5):
    print(messages[random.randint(0,len(messages)-1)],end='')
