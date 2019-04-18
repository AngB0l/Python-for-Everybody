#Ex1. Write a program to read through a file and print the contentsof the file (line by line) all in upper case.
# Example file  to transform in: www.py4e.com/code3/mbox-short.txt
fname = input('Enter a file name:\n')
try:
	fhand = open(fname)
except:
	print('File not found \n', fname)

for line in fhand:
	line = line.rstrip() #remove all \n char from the file because at the end print will add them again
	new = line.upper()
	print(new)

#Ex2. Write a program to prompt for a file name, and then read through the file and
# look for lines of the form: X-DSPAM-Confidence: 0.8475
fname = input('Enter a file name:\n')
if fname == '':
		fname = 'mbox-short.txt'
try:
	fhand = open(fname)
except:
	print('File not found ', fname)

for line in fhand: #type STR
	if not line.startswith('X-DSPAM-Confidence:'): continue
	line = line.rstrip() #type STR
	# start = line.split() #type LIST
	start = line.rfind(':') # start = 18: type INT
	print(start)
	print(line[start+1:])
	
#Ex3. Create an easter egg that apears when the user types 'na na boo boo'
fname = input('Enter a name: \n')
if fname == 'na na boo boo':
	print('na na boo boo to you\n')
	quit()
try:
	fhand = open(fname)
except:
	print('File not found\n')
for line in fhand:
	print(line)