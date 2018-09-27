#字典
myCat={'size':'fat','weight':100,'color':'white and black','age':5,10:'ten'}
print(myCat['color'])
print(myCat[10])

print('---------------------------')

a=[1,2,3]
b=[2,3,1]
print(a==b)

app={1:'a',2:'b',3:'c'}
bnn={2:'b',1:'a',3:'c'}
print(app==bnn)

'''
birthdays={'Alice':'Jan 1','Peter':'Feb 2','Bai':'June 16'}
while True:
    print('请输入姓名（输入回车退出）')
    name=input()
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name] + ' 是 ' + name+' 的生日')

    else:
        print('这里没有记录 '+name+' 的生日')
        print(name+' 的生日是？')
        birthday=input()
        birthdays[name]=birthday
        print('生日记录表已更新！')
'''


spam={'a':10,'b':'boy','c':'Mop'}

for k in spam.keys():
    print(k)

print('--------------------------')

for v in spam.values():
    print(v)

print('--------------------------')

for i in spam.items():
    print(i)

print('--------------------------')

#转换为列表
print(list(spam.keys()))
print(list(spam.values()))
print(list(spam.items()))

print('--------------------------')

spam={10:'abc','app':'apple','b':'banner','name':'Hawaii'}
for k,v in spam.items():
    print('键:'+str(k)+', 值:'+str(v))

print('--------------------------')

print(10 in spam.keys())
print('name' in spam)
print('apple' not in spam.values())

print('--------------------------')

#get()方法
have={'apple':20,'eggs':50,'dog':'Harry'}
print('我有 '+str(have.get('apple',0))+' 个苹果')
print('我有 '+str(have.get('cat','0只'))+' 猫咪')
print(have['dog'])

print('--------------------------')

pet={'color':'grey','age':5}
'''
print('朋友是 '+ pet.get('friend','Hawaoo'))
print('体重是 '+ pet.get('weight','500g'))
print('喜好是 '+ pet.setdefault('hobby','eating'))
print('年龄是 '+ str(pet.setdefault('age',10)))
print('年龄是 ' +str(pet.get('age',20)))
'''
print(pet.get('friend','Hawaoo'))
print(pet)

print(pet.setdefault('hobby','eating'))
print(pet)

print('--------------------------')

#计算每个字符出现的次数
message = '大家好啊，今天周五啊。'
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
print(count)

print('--------------------------')

for k,v in count.items():
    print(k+':'+str(v)+'次')

print('--------------------------')
print('--------------------------')

import pprint
pprint.pprint(count)