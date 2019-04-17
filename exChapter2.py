# Ex2. Write a program that uses input to prompt a user for their name and then welcomes them.
prompt = 'Enter your name:\n ' #\n means change the line(like Enter)
name = input(prompt)
print('Hello', name)
print('################')
################################
#Ex3. Write a program to prompt the user for hours and rate per hour to compute gross pay.
h = input('Hours:\n') #Type STR!
r = input('Rate:\n') #Type STR!

h = float(h) #1.The Transformation has to happen here. Declaring type before input does not work.
r = float(r) #2.The variable has to go in to the parenthesis otherwise this function assigns 0 to h and r
pay = 0.0
pay = h*r

print('Pay:', pay)
print('################')
################################
#Ex4. For the following expressions print the type and value
width = 17
height = 12.0

a = width // 2 # output: 17//2 = 8 INT
b = width // 2.0 # output: 17/2.0 = 8.5 FLOAT
c = height / 3 # output: 12.0 / 3 = 4.0 FLOAT
d = 1 + 2.0*5 # output: INT +FLOAT*INT = FLOAT
print('No class        value')
print('a', type(a) , a,'\n')
print('b', type(b) ,b, '\n')
print('c', type(c) ,c, '\n')
print('d', type(d) ,d, '\n')
print('################')
################################
#Ex5. Write a programm that takes Celsius as an input an prints Fahrehnheit
cel = input('Celsius:\n')
cel = float(cel)
far = cel*9/5 + 32
print('Fahrehnheit:', far)
print('################')
################################