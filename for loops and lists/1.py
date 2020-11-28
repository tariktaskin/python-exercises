"""Question 1:
Write the given 10 integer numbers in reverse.
"

# 1
def reverse_numbers(nums):
    nums = str(nums)
    nums = nums.split()
    return " ".join(nums[::-1])


print(reverse_numbers("3 6 9 12 15 18 21 24 27 30"))


