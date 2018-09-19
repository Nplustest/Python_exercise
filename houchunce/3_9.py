#try,except语句：异常处理
'''
def spam(num):
	try:
		return 100/num
	except ZeroDivisionError:
		print('Error: Invalid argument.')

print(spam(2))
print(spam(22))
print(spam(0))
print(spam(5))#执行此句
'''
'''
def spam(num):
	return 100/num

try:
	print(spam(2))
	print(spam(22))
	print(spam(0))
    print(spam(5))#不执行此句
except ZeroDivisionError:
	print('Error: Invalid argument.')
'''

#猜数字
import random
secret = random.randint(1,12)
print('I am thinking of a number between 1 and 12.')
for i in range(1,6):
	print('Take a guess.')
	guess = int(input())
	if guess > secret:
		print('Your guess is too high.')
	elif guess < secret:
		print('Your guess is too low.')
	else:
		break
if guess == secret:
	print('GOOD!')
else:
	print('The number I was thinking of was '+ str(secret))
