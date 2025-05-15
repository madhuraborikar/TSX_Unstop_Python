#To calculate the area and perimeter of a rectangle

#This program will ask the user to input the length and breadth of the rectangle
# and then calculate the area and perimeter of the rectangle.

# a = int(input("Enter the length of the rectangle: "))
# b = int(input("Enter the breadth of the rectangle: "))  
# Uncomment the above lines to get user input

a = 5  # Length of the rectangle
b = 3  # Breadth of the rectangle
#dont need to comment the above lines to get user input

# Calculate area and perimeter

# Area = length * breadth
area = a * b

# Perimeter = 2 * (length + breadth)
perimeter = 2 * (a + b) 

# Print the results
print("Area of the rectangle is:", area)
print("Perimeter of the rectangle is:", perimeter)