# Built-in Functions

#Returns the absolute value of a number

strvar11 = -500.8
abs(strvar11)

#Returns True if all items in an iterable object are true
#ERROR: TypeError: 'int' object is not iterable

strvar12 = 'string variable 12'
all(strvar12)

#Returns True if any item in an iterable object is true

strvar13 = 'string variable 13'
any(strvar13)

#Returns a readable version of an object. Replaces none-ascii characters with escape character

strvar14 = 'string varıable 14'
ascii(strvar14)

#Returns the boolean value of the specified object
#1:True and 0:False

strvar16 = 1
bool(strvar16)

#Returns a floating point number

numericvar1 = 1000
float(numericvar1)

#Returns an integer number

numericvar2 = 250.4
int(numericvar2)

#Returns the length of an object

strvar17 = 'it is string variable'
len(strvar17)

#Returns the smallest item in an iterable

strvar18 = '465329'
min(strvar18)

#Returns the highest item in an iterable

strvar19 = '465329'
max(strvar18)

#Returns a new string

numericvar4 = 400
str(numericvar4)

#Returns the type of an object

numericvar5 = 700
type(numericvar5)

#user defined functions

variable20 = 10
variable21 = 100

output = ((variable20+variable21)*100)/400 + variable20
print(output)

def calculator_function(variable20,variable21):
  """
  parameter: variable20, variable21
  return: Calculation of the given values
  """
  output_function = ((variable20+variable21)*100)/400 + variable20
  return output_function

#Call User Defined Function (calculator_function)
calculator_function(40,50)

#Default Function:
#Calculating the circumference of the circle

def circle_calculating(r,pi = 3.14):
  """
  input: r, pi
  return: calculating the circumference of the circle
  """
  output_circle = 2*pi*r
  return output_circle

#Call function
circle_calculating(2)

#Flexible Function:
"""def calculate(weight, height, *args):
  print(len(args))
  output_w = weight + height
  return output_w"""

def calculate(weight, height, *args):
  print(args)
  output_w = (weight + height)*args[1]
  return output_w

#Call function
#*args = 22,44
calculate(60,120,22,44)

# Lambda Function
#Enables us to write functions faster than other functions

output2 = lambda x: x*x
output2(3)
