#Ex1. Write a program that prints a list of x random numbers between min and max
#a. 5 random numbers between 0 and 1(default) and
#b. 5 random numbers between given min and max 
import random

x = input('How many random numbers do you want?\n')
x=int(x)
print(x,'Random numbers between 0 and 1:')
for i in range(x):
	numbersA = random.random() 
	print('a.',i,numbersA) #a.
	
fromNumber = input('What is the minimum numeric value that should be calculated\n')
toNumber = input('What is the maximum numeric value that should be calculated\n')
fromNumber = int(fromNumber)
toNumber = int(toNumber)
print(x,'Random numbers between min and max')
for i in range(x):
	numbersB = random.randint(fromNumber,toNumber) 
	print('b.',i,numbersB) #b.

#Ex2. Write a program to prompt for a score between 0.0 and 1.0 and calculate the grade.
#If the score is out of range print an error msg.
#>=0.9	A
#>=0.8	B
#>=0.7	C
#>=0.6	D
#<0.6	F

score = input('Please give a score between 0 and 1:\n')
try:
	score = float(score) #the transformation to FLOAT has to be here
	if score <= 1.0 and score >= 0.0:
		if score >=0.9: print('A')
		elif score >=0.8: print('B')
		elif score >=0.7: print('C')
		elif score >=0.6: print('D')
		else: print('F')
	else: print('Please give a number between 0 and 1.')
except: print('This is not a number')
