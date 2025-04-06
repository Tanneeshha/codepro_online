"""Task: Write a program that: 
1. Takes a string input from the user. 
2. Reverses the string. 
3. Checks if the original and reversed strings are the same (Palindrome check). """

string = input("Enter a string: ")
reverse = string[::-1]

if string == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")