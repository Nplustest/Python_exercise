import pprint
spam={'C':['a','b','c'],'A':'apple','B':'bnner',}
print(pprint.pformat(spam))
print('----------------------')
pprint.pprint(spam)

print('----------------------')
print('----------------------')

import pprint

message = 'ab bbaf。halfhfbjkag,fnajklgh'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1


pprint.pprint(count)

print('----------------------')
print('----------------------')

all={
    'Alice':{'apple':5,'banner':10},
    'Peter':{'egg':3},
    'Hawaii':{'apple':4,'egg':5},
    'Bai':{'orange':8,'banner':7,'apple':2,'pig':1}
}
#Alice，Peter。。每个人带来了什么

def totalBrought(name):
    for k,v in name.items():
        for i,j in v.items():
            print(k+'带来了'+str(j)+'个'+i)
totalBrought(all)

print('----------------------1')
print(all['Alice']['apple'])
print(len(all['Alice']))
print('----------------------2')
def totalBrought(name):
    thing=''
    for k,v in name.items():
        for i,j in v.items():
            thing=thing+str(j)+'个'+i+','
        print(k+'带来了'+thing[:-1])
totalBrought(all)

print('----------------------3')

#合并带来的东西
def totalFood(guests,food):
    sum = 0
    for k,v in guests.items():
        sum=sum+v.get(food,0)
    return sum

a='苹果有'+str(totalFood(all,'apple'))+'个'
b='香蕉有'+str(totalFood(all,'banner'))+'个'
print(a)
print(b)

print('----------------------4')

