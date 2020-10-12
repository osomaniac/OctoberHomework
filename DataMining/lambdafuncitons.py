## esentially creates a funciton in a variable
## lambdas process much much faster than functions

## create a multiplier
def testfunc(num):
    return lambda x : x * num

result1 = testfunc(10)
result2 = testfunc(1000)
print(result1(9))
print(result2(9))


## create a doubler and a tripler
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))


## filter funciton
## filters lists based on condition
numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)


## map function
## applies the lambda to each element in the list
numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]
mapped_list = list(map(lambda num: num % 2, numbers_list))
print(mapped_list)


## more examples with different amounts of arguments
x = lambda a : a + 10
print(x(5))

x = lambda a,b : a * b
print(x(5,6))

x = lambda a, b, c : a + b + c
print(x(5,6,2))
