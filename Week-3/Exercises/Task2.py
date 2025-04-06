#Extract the domain name from an email address (e.g., input: "user@example.com", output: "example.com"). 

email = input("Enter your email address: ")
print(f"The domain of given email '{email}' is: {email.split('@')[-1]}")