import math

def square(a):
    return math.ceil(a*a)

num_a = float(input("Введите длину стороны квадрата: "))
print(f"Округленная в большую сторону площадь квадрата: {square(num_a)}")
