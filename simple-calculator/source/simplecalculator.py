#Simple calculator program

#add function
def add(*nums):
    result = 0
    for num in nums:
        result += num
    return result
#multiplication function
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result
    
print(add(1,2))
print(add(-1,-1))
p#Simple calculator program

#add function
def add(*nums):
    result = 0
    for num in nums:
        result += num
    return result
#multiplication function
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result
    
print(add(1,2))
print(add(-1,-1))
print(add(1,2))
print(add(4,5))
print(add(1,2,3,4))

print(multiply(1,2))
print(multiply(1,2,3,4))
