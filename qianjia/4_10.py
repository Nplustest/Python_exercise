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
print(grid[1][1])
for i,j in grid:
    print()
'''


spam=[['A','B','C'],[10,20,30,40,50],['app','bnn']]
print(spam[0][0])
print(spam[0][1])
print(spam[0][2])
print(spam[1][0])
print(spam[1][1])
print(spam[1][2])
print(spam[1][3])
print(spam[1][4])

print('---------------------------')

for i in spam:
    for j in i:
        print(j,end='')
    print('')

print('---------------------------')

print('a','b','c','d',sep='$')

print('---------------------------')

