'''
spam=['Alice','Apple','Panda','Peter']
print('Alice' in spam)
print('AAA' not in spam)

print('----------------------------')

myPets=['Alice','Apple','Panda','Peter']
print('请输入宠物的名字：')
name=input()
if name in myPets:
    print(name+'是我的宠物')
else:
    print(name+'不是我的宠物哦~')
    print('我的宠物是：'+(",".join(myPets)))
'''

spam=['a','b','c']
#print(' '.join(spam))
#ABC=spam[0]
size=65
color='sdfs'
name='hhhh'
print(size)
size, color=color,size
print(size)

apple,book,cool=spam
print(apple)