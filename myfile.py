def incrementAndCheckEven(a):
    a = a + 1
    print("incremented value",a)
    if(a%2==0):
        print("Is even")
        return 1
    else:
        print("Is not even")

    return 0

a = incrementAndCheckEven(3)
print(a)