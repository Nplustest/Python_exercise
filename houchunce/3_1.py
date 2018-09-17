'''
#def语句定义函数
def hello():
	print('Hou') #函数体
	print('Chun')
	print('Ce')

hello()#输出三次定义的函数
hello()
hello()
'''

def hello(name):#name为变元=变量,保留在变元中的值在返回结果后会清除值。
	print('Hello ' + name)
	
hello('Chunce')
hello('Hou')
