#global语句
'''
def spam():
	global eggs
	eggs = '123'
	
eggs = '321'
spam()
print(eggs)
'''

def spam():
	global eggs
	eggs = '123'	
def bacon():
	eggs = '456'
def ham():
	print(eggs)
	
eggs = 789
spam()
print(eggs)