## esentially creates a funciton in a variable

def testfunc(num):
    return lambda x : x * num

result1 = testfunc(10)
result2 = testfunc(1000)
print(result1(9))
print(result2(9))


def myfunc(n):
    return lambda a : a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))


