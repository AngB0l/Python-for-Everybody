# Ex1. Write a program to prompt the user for hours and rate per hour to compute gross pay.
# An employee with more than 40 hours of works gats 1.5 times the hour rate for all overtime
hours=input('Give hours:\n')
rate = input('Give rate\n')
hours=float(hours)
rate=float(rate)
pay=0.0

if hours>40:
	pay = (hours-40)*rate*1.5 + 40*rate
else: 
	pay = hours * rate
print('To pay:',pay) 
print('################')
################################
# Ex2. Rewrite Ex1 but if the user does not give a number as an input print an Error Msg
hours=input('Give hours:\n')
rate = input('Give rate\n')
try:
	hours=float(hours)
	rate=float(rate)
	pay=0.0
	if hours>40:
		pay = (hours-40)*rate*1.5 + 40*rate
	else: 
		pay = hours * rate
	print('To pay:',pay)

except:
	print('Please give a number.') 
print('################')

################################
#Ex3. Write a program to prompt for a score between 0.0 and 1.0 and calculate the grade.
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
