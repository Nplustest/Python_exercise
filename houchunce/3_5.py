#可以同时存在多个局部变量，但是不会使用其他局部的变量
'''
def spam():
	hcc = 180
	chunce()
	print(hcc)
	
def chunce():
	haha = 100
	hcc = 108

spam()
'''
#全局变量可以在局部作用域使用
'''
def spam():
	print(eggs)
eggs = 11
spam()
print(eggs)
'''
#存在局部变量和全局变量都同名存在进行使用
'''
def spam():
	eggs = '1';
	print(eggs)
def bacon():
	eggs = '2'
	print(eggs)#2
	spam()#1
	print(eggs)
eggs = '3'
bacon()#2
print(eggs)#3
'''