'''
spam=['cat','dog','elephant','rat']
print('Hello '+spam[0])
print('Hello '+spam[-2])
print(spam[0:2])
print(spam[:2])
print(spam[1:])

print(len(spam))
print('---------------------')

spam[1]='miao'
print(spam)
print('---------------------')

a=['Alice','Linda','Peter']
b=['apple','oranger']
print(a+b)
print(b+a)
print(a*2)
print('---------------------')

name=['Haha','MAp','Wcc','Reta']
del name[1]
print(name)
'''

catNames=[]
while True:
    print('请输入第 '+str(len(catNames)+1)+' 只猫的名字（或者直接回车结束）：')
    name=input()
    if name=='':
        break
    catNames=catNames+[name]
print(catNames) #打印出来的是列表形式[]
for i in catNames:
    print(''+i)  #遍历出来