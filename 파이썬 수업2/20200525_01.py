#함수

def calc(x,y) :
    total = x + y
    print("In Functoion")
    print("a:" , str(a) , "b:" , str(b), "a+b:" , str(a+b), "total:",str(total))
    return total
a = 5
b = 7
total = 0
print("In Program - 1")
print("a:" , str(a) , "b:" , str(b), "a+b:" , str(a+b))
result = calc(a,b)
print("After Calc")
print("total:",str(total), "Sum:", str(result))