name='AbcdeFg'
print(name[5])
print(name[-2])
print(name[0:5])
print('abc'in name)
print('F' in name)
print(len(name))
for i in name:
    print('# # '+i+' % %')

for i in range(3):
    print(name)

print('----------------------------------------------')
#元组
eggs=('hello',100,'ABC')
print(eggs[0])
print(len(eggs))


a=('hello')
print(type(a))
b=('hello',)
print(type(b))

#元组，列表的转换
app=('A','hello',10)
bnn=['Boy',20]
print(list(app))
print(tuple(bnn))

spam=[0,1,2,3]
cheese=spam
cheese[0]='hello'
print(spam)
print(cheese)

le='left'
ri=le
le='right'
print(le)
print(ri)