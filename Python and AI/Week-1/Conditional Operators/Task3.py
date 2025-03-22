#Task 3: Compare the length of two strings.

# Method-1: Using separate variables to store string lengths
string1 = "Code"
string2 = "Pro"

length_string1 = len(string1)  # Calculate length of string1
length_string2 = len(string2)  # Calculate length of string2

res = length_string1 < length_string2  # Compare lengths

print(f"Length of string 1 is smaller than length of string 2: {res}") #display comaprision

# Method-2: Directly comparing string lengths within the print statement
string1 = "Code"
string2 = "Pro"

print(f"Length of string 1 is greater than length of string 2: {(len(string1) > len(string2))}")  #display comaprision

# Method-3: Using a boolean variable to store the comparison result
string1 = "Code"
string2 = "Pro"

is_greater = len(string1) < len(string2)  # Compare lengths and store in is_greater (variable)

print(f"Length of string 2 is greater than length of string 1: {is_greater}")  #display comaprision
