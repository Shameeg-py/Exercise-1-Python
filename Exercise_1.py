# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input("Enter your full name:  ")

# TODO: Ask the user for their age and store it in a variable
age = int(input("what is your age:  "))

# TODO: Print a greeting using the name and age variables 
print("Hello my name is", name, "i am", age, "years old.")

#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
Length = int(input("what is the length of the rectangle: "))
# TODO: Ask the user for the width of a rectangle and store it as an integer
Width = int(input("what is the Width of the rectangle: "))
# TODO: Calculate the area of the rectangle
area = Length * Width 
# TODO: Print the result
print(area)
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
Temp = float(input("what is the temperature:  " ))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
f = (Temp * 9/5) + 32

# TODO: Print the result rounded to two decimal places
Rounded_F = round(f, 2)
print(Rounded_F)