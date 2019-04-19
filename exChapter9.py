#Ex1. Write a program that reads the words in words.txt and stores them as keys in a dictionary.(www.py4e.com/code3/words.txt)
#It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
dct = dict()
fhand = open('words.txt')
for line in fhand:
	words = line.split()
	for word in words:
		if not word in dct:
			dct[word] = ""
print(dct)
print('Ex1 Done######################')
##############################################
#Ex2. Write a program that categorizes each mail message by which day of the week the commit was done.
#To do this look for lines that start with “From”, then look for the third word and 
#keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
#1.Find the appropriate lines
#2. Fill the dictionary with the days of the week as keys and the occuracies as valiues.
fhand = open('mbox-short.txt')
dct = dict()
for line in fhand:
	line = line.rstrip()
	words = line.split()
	if not line.startswith('From') :continue
	if len(words)<3 :continue
	days = words[2]
	#print(days)
	if days not in dct:
		dct[days] = 1
	else:
		dct[days] +=1
print(dct)
print('Ex2 Done######################')
##############################################
#Ex3. Write a program to read through a mail log, build a histogram using a dictionary to count 
#how many messages have come from each email address, and print the dictionary.
fhand = open('mbox-short.txt')
dct = dict()
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From'):continue
	words = line.split()
	if len(words)<3 : continue
	sender = words[1]
	if sender not in dct:
		dct[sender] = 1
	else:
		dct[sender] += 1
print(dct)
print('Ex3 Done######################')
##############################################
#Ex4. Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop 
# to find who has the most messages and print how many messages the person has.
fhand = open('mbox-short.txt')
dct = dict()
for line in fhand:
	line = line.rstrip()
	words = line.split()
	if not line.startswith("From"):continue
	if len(words)<3:continue
	sender = words[1]
	if sender not in dct:
		dct[sender] = 1
	else:
		dct[sender] += 1

biggestVal = None
for i in dct:
	if biggestVal == None or dct[i]>biggestVal:
		biggestVal = dct[i]
		name = sender
print(name,biggestVal)
print(dct)
print('Ex4 Done######################')
##############################################
#Ex5. This program records the domain name where the message was sent from instead of who the mail came
#from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.
fhand = open('mbox-short.txt')
dct = dict()

for line in fhand:
	line = line.rstrip()
	if not line.startswith('From'): continue
	words = line.split()
	if len(words)< 3 :continue
	#print(line)
	sender = words[1]
	splitmail = sender.split('@')
	#print(splitmail)
	dom = splitmail[1]
	#print(dom)
	if dom not in dct:
		dct[dom] = 1
	else:
		dct[dom] += 1
		
print(dct)
print('Ex5 Done######################')
##############################################