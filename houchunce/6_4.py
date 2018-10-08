#！ python3
#Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

t_list = text.split('\n')
for i in range(len(t_list)):
	t_list[i] = '* '+ t_list[i]#每行开头加上*
text = ('\n').join(t_list)

pyperclip.copy(text)


'''
tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
def printTable(tabledata):
        len_list = [0,0,0]
        for index, item in enumerate(tableData):
                for str in item:
                        if len(str) > len_list[index]:
                                len_list[index] = len(str)
        #print(len_list)

        for seq in range(len(tableData)):
                print(tableData[0][seq].rjust(len_list[0]),
                      tableData[1][seq].rjust(len_list[1]),
                      tableData[2][seq].rjust(len_list[2])
                      )
printTable(tableData)
'''