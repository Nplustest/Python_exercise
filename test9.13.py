'''
temp = input("��һ��1-10֮�����֣�")
guess = int(temp)
if guess == 8:
	print("��ܰ���Ŷ������ɶ��û�С�������")
else:
	if guess > 8:
		print("���˴���")
	else:
		print("С��С��")
'''




#coding:utf-8
"""--- ������ ---"""
temp = input("����һ��1-100֮������֣�")
guess = int(temp)
n = 66
count = 1
while guess != n and count <3:
	count = count+1
	temp = input("�´��ˣ����²°�")
	guess = int(temp)
	if guess == n:
		print("�¶���")
		print("�ܲ���Ŷ")
	else:
		if guess > n:
			print("���˴���")
		else:
			print("С��С��")
print("����")
