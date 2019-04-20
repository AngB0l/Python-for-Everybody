#Ex1. Revise a previous program as follows: 
# 1. In mbox-short.txt read and parse the “From” lines and pull out the addresses from the line. 
# 2. Count the number of messages from each person using a dictionary.
# 3. Print the person with the most commits (cwen@iupui.edu 5)

fhand = open('mbox-short.txt')
dct = dict()
for line in fhand:
	if not line.startswith('From'):continue
	words = line.split()
	if len(words)<3:continue
	#print(words)
	sender = words[1]
	#print(sender)
	if not sender in dct:
		dct[sender] = 1
	else:
		dct[sender] += 1
#print(dct)

lst = list()
for key,val in list(dct.items()):
	lst.append((val,key))
lst.sort(reverse = True)
count , mail = lst[0]
print(mail,count)
print('Ex1 Done######################\n')
############################################
#Ex2. This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the “From” line by finding the time string and then splitting that string into parts
# using the colon character. Print out the counts
fhand = open('mbox-short.txt')
dct = dict()
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From'):continue
	#print(line)
	words = line.split()
	if len(words)<3:continue
	#print(words)
	hms= words[5]
	#print(hms)
	i = hms.split(":")
	hour = i[0]
	#print(hour)
	if not hour in dct:
		dct[hour] = 1
	else:
		dct[hour] += 1

lst = list()
for key,val in list(dct.items()):
	lst.append((key,val))
lst.sort()
#print(lst)
for key,val in lst:
	print(key,val)
print('Ex2 Done######################\n')
############################################
#Ex3. Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter frequency varies between languages.
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
#Note: Encoding problems, works with: txt files with eng char
import string #used to remove all punctuation from the txt
from string import digits # used to remove all the digits from the txt
fname = input('Enter a file name: \n')
if len(fname) < 1 : fname = 'romeo.txt' #if the user doesn't type anything open romeo-full.txt
fhand = open(fname)
dct = dict()
for line in fhand:
	#line = line.lower() # I added it to the end of the next line to make the code shorter
	line = line.translate(str.maketrans('','',string.punctuation)).lower()
	line = line.translate(str.maketrans('','', digits)).rstrip()
	#print(line)
	words = line.split() #Input stiring Output list
	for word in words: #for each word in the line
		for abc in word: #for each letter of that word
			if not abc in dct: #if that letter doen't exist in the dictionary add it with val =1.
				dct[abc] = 1
			else:
				dct[abc] +=1 #else increase the value by one

lettersHist = list()
for key,val in list(dct.items()): #add everything to the list so that we can sort
	lettersHist.append((val,key))
lettersHist.sort(reverse = True) 
#print(lettersHist)

for val, key in lettersHist: #Make it pretty for the user
	print(key,val)
