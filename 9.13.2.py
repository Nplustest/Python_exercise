#coding:utf-8
"""--- 猜数字 ---"""
temp = input("输入一个1-100之间的数字？")
guess = int(temp)
while guess != 66:
    temp = input("猜错了，重新猜吧")
    guess = int(temp)

    if guess == 66:
        print("猜对了")
        print("很不错哦")
    else:
        if guess > 66:
            print("大了大了")
        else:
            print("小了小了")
print("结束")
