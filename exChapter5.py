#Ex1&2. Write a program which repeatedly reads numbers until the user enters “done”. 
#Once “done” is entered, print out the total, count,and average of the numbers.
#If the user enters anything other than a number, detect their mistake using try and except
# and print an error message and skip to the next number.
total = 0
i = 0
while True:
	val = input('Please give a number\n')
	if val =='q' or val=='quit' or val=='done': break #if the user types q or quit or done stop the while loop
	try:
		val = float(val)
		i +=1
		total = total + val
	except: print('This is not a number.Try again or type: q to quit.')
print('Numbers given:\n',i)
if i ==0 : print('Average is 0')
else : print('Average is:\n',total/i)
print('Sum is:\n',total)
print('################')
################################
#Ex2.Write a program which repeatedly reads numbers until the user enters “done”. 
#Once “done” is entered, print out the max and min of those numbers.
#If the user enters anything other than a number, detect their mistake using try and except
# and print an error message and skip to the next number.
max = None #We declare these values to type none so that we dont have to set a fixed max/min value
min = None
while True:
	val = input('Give a number:\n')
	if val=='q' or val=='quit' or val=='done': break
	try:
		val = float(val)
		if min is None or val<min: min = val
		elif max is None or val>max: max=val
	except:
		print('This is not a number.Try again or type: q to quit.')

print('Maximum value:',max)
print('Minimum Value:',min)
print('################')
################################


