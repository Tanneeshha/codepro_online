#Method: 1 Using for loop
def sum_nums(nums):
    return sum(num for num in nums if num % 2 == 0)  # Sum only even numbers

nums = [1, 0, 9, 4, 16, 99]
print(f"Sum of even numbers: {sum_nums(nums)}")  # Output: 20

#Method: 2 Using filter method
def sum_nums(nums):
    return sum(filter(lambda x: x % 2 == 0, nums))

print(f"Sum of even numbers: {sum_nums([7,8,6,4,4,2,9])}")  # Output: 24

#Method: 3 Using for loop (detailed)
def sum_nums(nums):
    total = 0  # Start with 0
    for num in nums:  # Go through each number
        if num % 2 == 0:  # Check if it's even
            total += num  # Add it to total
    return total  # Return the final sum

numbers = [2,10,4,5,1,1,3]
print(f"Sum of even numbers: {sum_nums(numbers)}")  # Output: 16
