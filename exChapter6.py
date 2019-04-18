#Ex1. Write a while loop that starts at the last character in the string and works its way backwards
# to the first character in the string, printing each letter on a separate line, except backwards.
text = input('Type something to print backwards:\n')
i=len(text)
while i >= 1:
	letter = text[i-1]
	print(letter)
	i=i-1
print('#############')
######################################
#Ex3. Ask the user for a character and a text. 
#Create a function that counts the times that the character appears in the string

def count(searchTerm,text):
	occurrences = 0
	for i in text:
		if i ==searchTerm:
			occurrences+=1
	return occurrences #saved in: found

searchTerm = input('What do you want to search for?\n') #has to be ONE letter or number
text = input('And now the text to search in \n')
found = count(searchTerm,text)
print(found)
print('#############')
######################################
#Ex4. Rewrite the previous exersise but use the STR method: count
#NOTE. if the search term is 11 in 111 it will find 1
searchTerm = input('What do you want to search for?\n') #go wild with letters or numbers
text = input('And now the text to search in \n')
occurrences = text.count(searchTerm)
print(occurrences)
print('#############')
######################################
#Ex5. Take the following Python code that strores a string: str = 'X-DSPAM-Confidence:0.8475'
#Use find and string slicing to extract the portion of the string after thecolon character
# and then use the float function to convert the extracted string into a floating point number.
text = 'X-DSPAM-Confidence:0.8475'
beg = text.find(':') # beg = 18, the possision of the ':'
number = text[beg+1:] # in the 'text' string [from possision(18+1) : end possision(NULL)]
print(float(number)) #print the number and transform it to float at the same time
print('#############')
######################################
