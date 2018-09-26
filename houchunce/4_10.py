'''
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]
list_len = len(grid)
list_col = len(grid[0])
for i in range(list_col):
	for j in range(list_len):
		print(grid[j][i],end = '')
	print()


spam = ['apples', 'bananas', 'tofu', 'cats']
def adc(data):
	list_len = len(data)
	s = ''
	for i in range(list_len-1):
		s=s+str(spam[list_len-1])+','
	s=s+'and '+str(spam[-1])
	return s
s=adc(spam)
print(s)
'''
