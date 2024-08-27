def incrementAndCheckEven(a):
    a = a + 1
    print("incremented value",a)
    if(a%2==0):
        print("Is even")
    else:
        print("Is not even")

    return a//2

a = incrementAndCheckEven(3)
