temp = input("猜一个1-10之间数字：")
guess = int(temp)
if guess == 8:
	print("你很棒棒哦，但是啥都没有。哈哈哈")
else:
	if guess > 8:
		print("大了大了")
	else:
		print("小了小了")
