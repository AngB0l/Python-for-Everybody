#Ex1. Write a function called chop that takes a list and modifies it, removing the first and 
#last elements, and returns None. 
#Then write a function called middle that takes a list and returns a new list 
# that contains all but the first and last elements.
def chop(lista): #this way modifies the original list
	del lista[len(lista)-1]
	del lista[0]

def middle(listb): #this way it keeps the original list as it is and returns a new modified one
	return listb[1:len(listb)-1]


alist = ['a','h','e','y','x']
chop(alist)
blist = ['w','y','o','u','t']
storeList = middle(blist)

print(alist)
print(storeList)
print(blist)
print('######################')
##############################################
#Ex4. Write a program to open the file romeo.txt and read it line by line. (www.py4e.com/code3/romeo.txt)
#For each line, split the line into a list of words using the split function.
#For each word, check to see if the word is already in a list. If the word is not in the list, 
#add it to the list. When the program completes, sort and print the resulting words in alphabetical order.
fhand=open('romeo.txt')
listA = list()
for line in fhand:
	words=line.split()
	for word in words:
		if word not in listA:
			listA.append(word)
listA.sort()
print(listA)
print('######################')
##############################################
#Ex5. Write a program to open the file mbox-short.txt, find the lines that start with From, 
# then count the results and print the sender's address
fhand = open('mbox-short.txt')
i=0
for line in fhand:
	line = line.strip()
	
	if not line.startswith('From') :continue #still a STR
	words = line.split() #words type: LIST
	if len(words) < 3 :continue #or i could put 'From:' in the line with .starts with but the exercise say not to
	i+=1
	print(words[1])
print('There where %d lines with From as the first word' % i)
print('######################')
##############################################
#Ex6. Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at
#the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the 
#max() and min() functions to compute the maximum and minimum numbers after the loop completes.
lst = list()
while True:
	inp = input('Please give a number or type q:')
	if inp == 'q' or inp == 'done': break
	try :
		inp = float(inp)
		lst.append(inp)
		large = max(lst)
		small = min(lst)
	except : print('This is not a number')
if len(lst) == 0 : print('No numbers found :(')
else: print('Max is %g, and min is %g' % (large,small))