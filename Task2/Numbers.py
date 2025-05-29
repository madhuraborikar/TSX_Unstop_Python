''' Write a script that takes two numbers as input and prints whether 
 the first number is greater than, less than, or equal to the second 
 number. 1'''

# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Compare the numbers

#If Number 1 is greater than Number 2
if num1 > num2:
    print(f"{num1} is greater than {num2}.")

    #If Number 2 is Greater than Number 1
elif num1 < num2:
    print(f"{num2} is greater than {num1} ")   
else:

    #If both are equal
    print("Both are equal.")