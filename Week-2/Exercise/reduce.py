from functools import reduce

nums = [9, 10, 15, 4, 1, 6]
largest_num = reduce(lambda a, b: a if a > b else b, nums)

print(f"Largest number from {nums} is {largest_num}")
