# 239 < 30 потому что первое число числа(3)0 больше числа (2)39 , так же и с буквами
#   функция len кол-во символов в слове считает


# вычислять площадь треугольника по трём сторонам.
# S =p(p−a)(p−b)(p−c)               #-площадь
# p = (a + b + c)/2                 # – полупериметр треугольника.
a = int(input())
b = int(input())
c = int(input())

p = (a + b + c)/2
s = ((p*(p - a) * (p - b) * (p - c)) ** 0.5)
print(s)

###################### Напишите программу, принимающую на вход целое число,которая выводит True, если переданное значение попадает в интервал
# (−15,12]∪(14,17)∪[19,+∞) и False в противном случае (регистр символов имеет значение).

# a = int(input())
# if  -15 < a <=12 or (14 < a < 17) or (19 <= a):
#     print(True)
# else:
#     print(False)

##################### передача переменной в строку
# S = 1123
# print(f"s={S}")