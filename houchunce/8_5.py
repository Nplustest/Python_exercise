#! python3
#creates quizzes with questions and answers in random order, along with the answers key.

import random

#创建字典，存储key和values值
capitals = {'Alabama':'Montgonmery','Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New150 Python Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville','Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#创建35份文件
for quizNum in range(35):
	#创建文件
	quizFile = open('capitalizequiz%s.txt' 	%(quizNum+1),'w')
	answerKeyFile = open('capitalizequiz_answers%s' %(quizNum+1),'w')
	
	#文件开头写入个人信息属性
	quizFile.write('Name:\nDate:\nPeriod:\n\n')
	quizFile.write((' '*20)+ 'State Capitals Quiz (Form %s)' %(quizNum+1))
	quizFile.write('\n\n')
	
	#随机排序字典中key
	states = list(capitals.keys())
	random.shuffle(states)
	
	#创建问题
	for questionNum in range(50):
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers,3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)
	
	#写入问题和答案到文件中
		quizFile.write('%s. What is the callable of %s?\n'%(questionNum+1,states[questionNum]))
		for i in range(4):
			quizFile.write('%s.%s\n' %('ABCD'[i],answerOptions[i]))
		quizFile.write('\n')
	
		answerKeyFile.write('%s.%s\n' %(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()