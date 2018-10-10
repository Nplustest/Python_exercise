#! python3
# Finds phone numbers and email addresses on the clipboard.

import pyperclip,re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\)\)?		#区号格式判断可为空
	(\s|-|\.)?				#区号后的符号判断
	(\d{3})					#前三个号码判断
	(\s|-|\.)				#第一段号码后的符号判断
	(\d{4})					#后四个号码判断
	(\s*|(ext|x|ext.)\s*(\d{2,5}))?		#尾部的格式判断可为空
	)''',re.VERBOSE)

emailRegex = re.compile(r'''(
	([a-zA-Z0-9.+-%_])+		#邮箱用户名校验
	@						#分隔符@验证
	([a-zA-Z0-9.+-%_])+		#邮箱域名校验
	(\.[a-zA-Z0-9]{2,4})	#邮箱后缀校验
	)''',re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[6] != '':
		phoneNum += ' x' + groups[6]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups)
	
if len(matches)>0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('null')
	
#numRegex = re.compile(r'^\d{1,3}(,{3})*$')
#nameRegex = re.compile(r'[A-Z][a-z]*\sNakamoto')
#yRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs),re.I')