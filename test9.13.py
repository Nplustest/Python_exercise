'''
temp = input("猜一个1-10之间数字：")
guess = int(temp)
if guess == 8:
	print("你很棒棒哦，但是啥都没有。哈哈哈")
else:
	if guess > 8:
		print("大了大了")
	else:
		print("小了小了")
'''




#coding:utf-8
"""--- 猜数字 ---"""
temp = input("输入一个1-100之间的数字？")
guess = int(temp)
n = 66
count = 1
while guess != n and count <3:
	count = count+1
	temp = input("猜错了，重新猜吧")
	guess = int(temp)
	if guess == n:
		print("猜对了")
		print("很不错哦")
	else:
		if guess > n:
			print("大了大了")
		else:
			print("小了小了")
print("结束")
