#coding:utf-8
"""--- ������ ---"""
temp = input("����һ��1-100֮������֣�")
guess = int(temp)
while guess != 66:
    temp = input("�´��ˣ����²°�")
    guess = int(temp)

    if guess == 66:
        print("�¶���")
        print("�ܲ���Ŷ")
    else:
        if guess > 66:
            print("���˴���")
        else:
            print("С��С��")
print("����")
