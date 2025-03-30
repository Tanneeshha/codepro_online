def is_even(n):
    if n%2==0: return True
    else: return False

num = int(input("Enter any number: "))
print(f"{num} is even? {is_even(num)}")