def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	else:
		return True
'''	
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('4aa-saas-qwe is a phonr number:')
print(isPhoneNumber('4aa-saas-qwe'))
'''
message = 'Call me at 415-555-1456 tomorrow. 415-555-8879 is my office.'
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('Phone number found: '+ chunk)
print('Done')
