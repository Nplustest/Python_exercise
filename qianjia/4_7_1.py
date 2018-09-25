def eggs(parameter):
    parameter.append('hello')
spam=[1,2,3]
eggs(spam)
print(spam)

#copy
import copy
spam=['A','B','C']
cheese=copy.copy(spam)
cheese[1]=500
print(spam)
print(cheese)

