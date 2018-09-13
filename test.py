'''
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")
'''

num=int(input('请输入数字：'))
if num%2==0:
    if num%3==0:
        print('可以整除2和3')
    else:
        print('可以整除2，但不可以整除3')
else:
    if num%3==0:
        print('可以整除3，但不可以整除2')
    else:
        print('不能整除2和3')