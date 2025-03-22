#Task 4: Use >= to check if a person is eligible to vote (age >= 18).

#Ask name from user
name = input("Enter your name here: ")

# Ask for user's age
age = int(input("Enter your age here: "))  

# Print result
print("Analyzing can you vote....")
print("If true then you are eligible if false then you must be below 18.")

# Check eligibility
eligible = age >= 18  

print(f"{name} is eligible to vote. {eligible}")