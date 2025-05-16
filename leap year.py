'''Write a script that checks if a given year is a leap year (divisible by 
4, but not by 100 unless also divisible by 400). 1'''


# Function to check if a year is a leap year
def is_leap_year(year):
    # Leap year if divisible by 4 and (not divisible by 100 or divisible by 400)
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Example usage
# Get user input
year = int(input("Enter a year: "))
# Check if the input is a valid year
if year < 0:
    print("Please enter a valid year.")
    year = int(input("Enter a valid year: "))
# Print the result
# Check if the year is a leap year

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")