'''
#pprint(),pformat()函数输入结果换行
import pprint
message = 'It was a bright cold day in April,and the clocks were striking thirteen.'
count = {}
for char in message:
	count.setdefault(char,0)
	count[char] = count[char]+1
	
pprint.pprint(count)
#print(pprint.pformat(count))

##字棋盘
theBoard = {'top-L':' ','top-M':' ','top-R':' ',
			'mid-L':' ','mid-M':' ','mid-R':' ',
			'low-L':' ','low-M':' ','low-R':' '}
def printBoard(board):
	print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
	print('-+-+-')
	print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
	print('-+-+-')
	print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])
turn = 'X'
for i in range(9):
	printBoard(theBoard)
	print('Turn for '+turn+' .Move in which space?')
	move = input()
	theBoard[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
printBoard(theBoard)

all = {'Alice':{'apples':5,'pretzels':12},
		'Bof':{'ham sandwiches':3,'apples':2},
		'Hou':{'cups':3,'apple ples':1},
		'Chunce':{'apple':1,'pretzels':3}}

def totalBrought(guests,name):
	num = 0
	for k,v in guests.items():
		num = num + v.get(name,0)
	return num
	
print('apples '+str(totalBrought(all,'apples')))
print(all['Alice'])
'''
#stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(inventory):
	count = 0
	for k,v in inventory.items():
		print(str(v)+' '+k)
		count += v
	print('物品总数:'+str(count))
#displayInventory(stuff)

def addToInventory(inventory,addedItems):
	for item in dragonLoot:
		if item not in inventory.keys():
			inventory.setdefault(item,1)
		else:
			inventory[item] += 1
			
inv = {'gold coin':42,'rope':1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin']
inv = addToInventory(inv,dragonLoot)
print(inv)
displayInventory(inv)