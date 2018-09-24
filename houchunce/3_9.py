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
'''
#Collatz序列
'''
def collatz(number):
	if (int(number)%2) == 0:
		return number//2
	elif (int(number)%2) == 1:
		return 3*number + 1
'''

def collatz(number):
        while number != 1:            
                if number % 2 == 0:
                        number = number // 2        
                        print (number)
                elif number % 2 == 1:
                        number = 3*number+1
                        print (number)
while True:
        try:	
                number = int(input('Enter a number: '))
                print (number)
                collatz(number)
        except ValueError:
                print('Not a integera. Please input a integera.')



