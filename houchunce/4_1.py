'''
spam = ['cat','bat','rat','elephant']
print(spam[0])
print(spam[-2])
print(spam[1:3])
print(['cat','bat','rat','elephant'][3])
print('Hello ' + spam[0])
print('The ' + spam[1] + ' ate the ' + spam[0] +'.')

spam = [['cat','bat'],[10,20,30,40]]
print(spam[0])
print(spam[1][3])

spam = ['a','b','c']
print(len(spam))
spam[1] = 'd'
print(spam[1])
spam = spam + [1,2,3]
del spam[1]


catNames = []
while True:
	print('输入第'+str(len(catNames)+1)+'只猫的名字（输入空格退出）:')
	name = input()
	if name == '':
		break
	catNames = catNames + [name]#保存用户输入的参数到catNames
print('猫的名字有：')
for name in catNames:
	print(name)

supplies = ['pens','staplers','flame-throwers','binders']
for i in range(len(supplies)):
	print('Index '+str(i)+' in supplies is:'+supplies[i])

myPets = ['ZhuDa','ZhuEr','ZhuSan']
print('请输入你家猪的名字：')
name = input()
if name not in myPets:
	print('你家猪不在我家猪圈里。')
else:
	print(name +'在我家猪圈里.')
'''
#多重赋值
#cat = ['a','b','c']
#A,B,C = cat