
#Numeric variable

#integer
variable100 = 100
variable200 = 200
variable300 = 300
variable400 = 400

#float
variable500 = 500.5
variable600 = 600.9
variable700 = 700.4

#print variable

print("Integer Variables: {}, {}, {}, {}".format(variable100, variable200, variable300, variable400))
print("Float Variables: {}, {}, {}".format(variable500, variable600, variable700))

#Four transactions

#Addition
print("Addition:", variable100 + variable200 + variable300)

#Subtract
print("Subtract:", variable400 - variable300)

#Division
print("Division:", variable400 / variable200)

#Multiply
print("Multiply:", variable400 * variable100)

#Addition, subtract, division and multiply
new_value = ((variable400 + variable300) * (variable500 + variable700) / variable600) - variable400
print("Output: {}".format(new_value))

#if-else

if variable400 == 400:
  x = variable400 + 200
  if x == 600:
    print("Output: {}".format(x))
else:
  print(" ")

#input if-else

enter_value = int(input("Enter a value:"))

if enter_value >= 200:
  print(enter_value * 5)
elif enter_value <= 200:
  print(enter_value * 10)
else:
  print(" ")

#string variable

str_variable1 = "banana"
str_variable2 = "apple"
str_variable3 = "cherry"
str_variable4 = "500"
str_variable5 = "100"

#print string variable

print(str_variable1)
print(str_variable1, "and", str_variable2)
print(str_variable4 + str_variable5)

#if-else and input

enter_stringvalue = input("Enter String Value:")
print("Entered Value:", enter_stringvalue)

if len(enter_stringvalue) >= 10:
  print("More than 10 characters")
else:
  print("Less than 10 characters")
