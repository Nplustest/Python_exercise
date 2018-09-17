#return语句指定返回值
import random
def Num(num):
	if num == 1:
		return '壹'
	elif num == 2:
		return '贰'
	elif num == 3:
		return '叁'
	elif num == 4:
		return '肆'
	elif num == 5:
		return '伍'
	elif num == 6:
		return '陆'
	elif num == 7:
		return '柒'
	elif num == 8:
		return '捌'
	elif num == 9:
		return '玖'
#获取1-9之间的随机整数赋值于num
print(Num(random.randint(1,9)))
