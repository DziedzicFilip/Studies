import random

# lista = [3,5,4,78,3]
# z1, *z2 = lista 
# print(z1)
# print(z2)

def f(**element):
    print(element)
    a = element.get('a')
    b = element.get('b')
    return a + b, a * b, a % b

def f2():
    randomnumber = [random.random() for i in range(7)]
    return randomnumber
def f3():
    randomnumber = [x**2 for x in range(1,40) if x%2 != 0 ]
    return randomnumber


if __name__ == '__main__':
    result = f(a=3, b=4)
    print(result)
    # print(f(a=3,b=4))
    # z1, *z2 = f(a=3, b=4)
    # print(z1, z2)
    a = f2()
    print(a)
    b = f3()
    print(b)