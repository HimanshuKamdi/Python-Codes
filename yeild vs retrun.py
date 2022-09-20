def square(nums):
    for num in nums:
        yield num**2
def squares(nums):
    for num in nums:
        return num**2

print(square([1,2,3,4]))
print(squares([1,2,3,4]))