#! python3
# An insecure password locker program.
password = {'Email':'adc123',
			'QQ':'abc456',
			'Wechat':'abc789'}
			
import sys,pyperclip
if len(sys.argv) < 2:
	print('Usage:py pw.py [account] - copy account password')
	sys.exit()
	
account = sys.argv[1] #获取第一个输入的参数

if account in password.keys():
	pyperclip.copy(password[account])
	print('成功复制'+account+'的值')
else:
	print('没有'+account+'账号')
