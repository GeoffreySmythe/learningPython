# Basics, Python 3, high-level, simplistic
# Print Function, Strings, Conversion
'''

print ('This is an example of print function')
print ("This is an example of print function")
print ('We\'re going to the store') # -> We're going to the store, use '' at all times

print ('Hi ' + 'there')
print ('Hi', 'there')
print ('Hi', 5)
print ('Hi ' + str (5))
print (int ('8') + 5)
print (float ('8.5') + 5)
'''
# Operators + - * /
# Single line comment, ''' multiple line comments
'''
print (5.0/34.0)        # 0.147058823529
print (4**4)            # 4 to the power of 4
print (5/2)             # 2
'''
# Variables
'''
variable = 55 + 22
print (variable)
x, y = (3, 5)

print (x + y)
'''
# While loop
'''
condition = 1

while condition < 10 :
    print (condition)
    condition += 1

while True:
    print ('doing stuff')
'''

# For loop
'''
condition = 1

exampleList = [1,2,3,4,5,6,7,7,4,5,4,5]

for eachNumber in exampleList:
    print (eachNumber)
    print ('continue program')

for x in range(1, 11):
    print (x)
'''
# If, else, elif statement
'''
x = 5
y = 8
z = 5
a = 3

if z < y > x > a:
    print ('y is greter than z and greater than x')

if z == x:
    print ('z is equal to x')

if x > y:
    print ('x is greater than y')
else: 
    print ('x is not greater than y')

x = 5
y = 10 
z = 22

if x > y:
    print ('x is greater than y')
elif x < z:
    print ('x is less than z')
else:
    print ('if and elif never ran')
'''
# Functions, Parameters, Default Function Parameters
'''
def exampleFunction ():
    print ('bang')
    z = 3 + 9
    print (z)

def addition (num1, num2):
    answer = num1 + num2

def simple (num1, num2 = 5):
    print (num1, num2)

def basic_window (width, height, font = 'TNR', bgc = 'w', scrollbar = True):
    print (width, height, font, bgc, scrollbar)

basic_window (100, 200, scrollbar = False)
'''

# Global and Local Variables
'''
x = 6

def example():
    global x
    x += 6
    print (x)

def someExample():
    globx = x
    globx += 5
    return globx

myVariable = someExample()

print (myVariable)
'''

# Writing to File, Appending Files, Read from a file
'''
text = 'Sample Text to Save\nNew List!'

saveFile = open ('exampleFile.txt', 'w')
saveFile.write (text)
saveFile.close()

appendMe = '\nNew bit of information'
appendFile = open ('exampleFile.txt', 'a')
appendFile.write (appendMe)
appendFile.close()

readMe = open ('exampleFile.txt', 'r').readlines()
print (readMe)
'''

# Classes
'''
class calculator:

    def addition(self,x,y):
        added = x + y
        print(added)
        
    def subtraction(self, x,y):
        sub = x - y
        print(sub)

    def multiplication(self,x,y):
        mult = x * y
        print(mult)

    def division(self,x,y):
        div = x / y
        print(div)

myCalculator = calculator()
myCalculator.subtraction (11, 2)
'''
# If module is used in other script, this would not run
'''
if __name__ == '__main__':
    print ('such great module!!!')
'''
# Getting user input

x = raw_input ('What is your name? ')
print ('Hello ', x)