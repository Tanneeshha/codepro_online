#Write a Python script to extract the first and last word from a sentence entered by the user. 

text = input("Type anything here: ") 
print(f"The first word in the given sentence is: {text.split()[0]}")
print(f"The last word in the given sentence is: {text.split()[-1]}")