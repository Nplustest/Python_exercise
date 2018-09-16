'''
print('Hello! WHat is your name?')#获取键盘输入的name
myName = input()
print('It is good to meet you, ' + myName)#输出获取的name
print('The length of your name is:')#len()函数计算myName的字符长度
print(len(myName))
print('What is your age?')#获取键盘输入的age
myAge = input()
print('You will be '+ str(int(myAge) + 1) + ' in a year.')#把age加1转化为str类型输出
'''

#round()函数取小数点后几位
#round(10/3,3) #3.333
#round(0.5) #0