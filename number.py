#AMIR ABDULA  

def bisectionMet(func, a , b ):
    funca = func(a)
    funcb = func(b)

    if funca * funcb > 0:
        print("function a and function b  must have different signs !")
        return None

    for _ in range(50):
        mid = (a + b) / 2
        funcc = func(mid)

        if funcc == 0:
            return mid
        if funca * funcc > 0:
            a = mid
            funca = funcc
        if funcb * funcc > 0:
            b = mid
            funcb = funcc

    return mid


func = lambda x: x**3 - 3 * x

a=1
b=3
print(f"Interval : {a,b}")
x = bisectionMet(func, a, b)
print("last mid-point is :")
print(x)
