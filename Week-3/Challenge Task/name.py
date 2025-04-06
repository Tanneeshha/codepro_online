#Problem: Create a Python script that asks the user for their full name, removes any extra spaces, and then 
# displays the following: 
# ● The full name in uppercase. 
# ● The full name in lowercase. 
# ● The number of characters (excluding spaces). 
# ● The first and last name separately. 

name = input("What is your full name? ")
name = name.strip()
count = len(name.replace(" ", ""))  # count characters excluding spaces
print(f"See how {name} looks like in uppercase: {name.upper()}")
print(f"See how {name} looks like in lowercase: {name.lower()}")
print(f"The number of characters in {name} is: {count}")
print(f"Your first name is: {name.split()[0]}")
print(f"And your last name is: {name.split()[1]}")