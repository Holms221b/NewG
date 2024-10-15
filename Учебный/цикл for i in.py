# for i in 2,3,5:
#     print(i*i)
#from lib2to3.pgen2.tokenize import

# for i in range(10):
#     print(i*i)
#

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for x in range(c,d+1): # второй отрезок
#   print('\t',x, end='')
# for y in range(a,b+1): # первый отрезок
#   print('\n',y, end='')
#   for x in range(c,d+1): # второй отрезок
#     print('\t', y*x, end='')


# a = input().split() ###### сумма нечетных чисел которые в отрезке
#
# num = int(a[0])
# un =  int(a[1])
# # a = int(a)
# # b = int(b)
# s = 0
# u = max(num,un)
# p = min(num,un)
# for i in range(p,u + 1):
#   if i % 2 != 0:
#     s+= i
# print(s)


# a = int(input()) ################ найти среднее арифметическое кратное на 3
# b = int(input())
# x = 0
# y = 0
# for i in range(a,b +1):
#   if i % 3 == 0:
#     x += i
#     y += 1
# print(x / y)




# a = int(input())################## найти среднее арифметическое кратное на 3 при помощи листа
# b = int(input())
#
# mass = []
#
# for i in range(a,b + 1):
#   if i % 3 == 0:
#     mass.append(i)
# print(sum(mass) // len(mass))


