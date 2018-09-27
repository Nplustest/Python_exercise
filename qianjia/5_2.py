import pprint
spam={'C':['a','b','c'],'A':'apple','B':'bnner',}
print(pprint.pformat(spam))
print('----------------------')
pprint.pprint(spam)

print('----------------------')
print('----------------------')

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:     count.setdefault(character, 0)
count[character] = count[character] + 1

pprint.pprint(count)