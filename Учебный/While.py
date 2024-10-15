# a = 100
#
# while a >= 50:
#     print(a,end=' ')
#     a -= 1
#
#
# b = 5
# while b <= 55:
#     print(b)
#     b += 2

# i = 0
# a = 0
# while i <= 10:
#     a +=1
#     i = i + 1
#     if i > 7:
#         i = i + 2
# print(a)

# n = int(input())
# c = 1
# while c <= n:
#     print('()' * c)
#     c += 1

# n = int(input())
# stars = "*"
# while len(stars) <= n:
#     print(stars)
#     stars += "*"

# i = int(input())
# a = int(input())
# print(i % a)

# i = 0 ################ Сколько всего знаков * будет выведено после исполнения фрагмента программы:
# while i < 5:
#     print("*")
#     if i % 2 == 0:
#         print("**")
#     if i > 2:
#         print("***")
#     i = i + 1


# i = [3,4,5,6,7]                ################ среднее значение суммы цифр
# avg = sum(i) / len (i)
# print(f"Среднее значение: {avg}")

# a = int(input())############# по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.
#
# i = 0
# while a != i:
#     i += a
#     a = int(input())
# print(i)


# a = int(input()) ############### пирог разделить на 2 команды (общее минимальное число разделить на 2 числа)
# b = int(input())
# c=1
# while c%a !=0 or c%b!=0:
#     c=c+1
# print(c)

# i = 0
# while i < 5:
#     g = input().split()
#     a = int(g[0])
#     b = int(g[1])
#     print(a * b)
#     i += 1

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)

n = int(input()) ###### число меньше 10 и больше 100
while n < 100:
    if n < 10:
        n = int(input())
        continue
    else:
        print(n)
        n = int(input())
