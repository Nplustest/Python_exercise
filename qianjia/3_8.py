'''
def spam():
    print(eggs)
eggs=100
spam()
print(eggs)

print('--------------------')

'''

'''
def spam():
    eggs=50
    bacon()
    print(eggs)

def bacon():
    ham=20
    eggs=5
    print(eggs)
spam()
bacon()

print('--------------------')
'''

'''
def spam():
    eggs='spam家的鸡蛋'
    print(eggs)
def bacon():
    eggs='bacon家的鸡蛋'
    print(eggs)
    spam()
    print(eggs)
eggs='谁家的鸡蛋啊'
bacon()
print(eggs)

print('--------------------')
'''

'''
def spam():
    global eggs
    eggs='spam家的鸡蛋'
def bacon():
    eggs='bacon家的鸡蛋'
def ham():
    print(eggs)
eggs=42
spam()
print(eggs)
'''

#会报错
'''
def spam():
    print(eggs)
    eggs = 'spam家的鸡蛋'
eggs='鸡蛋'
spam()
'''

#猜数字
import random
num=random.randint(1,20)
print('请输入1到20的整数')
for guessTaken in range(1,7):
    print('请开始你的表演，你一共有6次机会猜哦！')
    guess=int(input())

    if guess < num:
        print('你猜的太小了')
    elif guess > num:
        print('你猜的太大了')
    else:
        break
if guess==num:
    print('恭喜你猜对了！')
else:
    print('机会用完了，没有猜对哦')