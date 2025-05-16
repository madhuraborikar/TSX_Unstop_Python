
'''Write a script that concatenates two strings and prints the result. '''

# User Input two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the input is valid
if not string1 or not string2:
    print("Please enter valid strings.")
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    
# Check if the strings are empty
if string1 == "" or string2 == "":
    print("Strings cannot be empty.")
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")



# Concatenate the strings
result = string1 +" "+ string2

# Print the result
print("Concatenated string:", result)
