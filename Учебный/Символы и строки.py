# a = "Футбол"
#
# for i in range(6):
#     print(a[i],end="")

# a = "Футбол"
#
# for i in a:
#         print(i,end="")

# a = input() ############################# количество "C" в строке
# c = 0
#
# for nucl in a:
#     if nucl == "C":
#         c += 1
# print(c)

# ball = input()     ########################## количество "C" в строке
# print(ball.count("G"))

# n = list(input())###################### программу, которая вычисляет процентное содержание символов
# c = n.count('c') + n.count('C')
# g = n.count('g') + n.count('G')
# v = len(n)
# print((c+g)/v*100)

# n = list(input())###################### программу, которая вычисляет процентное содержание символов
# d = ["c", "C", "g", "G"]
# s = 0
# v = len(n)
# for i in n:
#     for x in d:
#         if i == x:
#             s += 1
# print(s/v*100)



#import re      #####################################программу, которая вычисляет процентное содержание символов(библиотека)
# x = input()
# print(len(re.findall("(c|C|g|G)", x)) / len(x) * 100)


# s = 'abcdefghijk'           ####### срезы Slicing задаем диапазон
# print(
# s[3:6],
# s[:6],
# s[3:],
# s[::-1],
# s[-3:],
# s[:-6],
# s[-1:-10:-2])

# i = input()
# r = i [::-1]
# if r == i:
#     print("YES")
# else:
#     print("NO")


# s = list(input())
# #v = len(s)
# x = 0
# for m in s:
#     if m == s:
#         x += 1
#
# # a = s.count[::-1]
# # for i in range( +1):
#
#
# print(x)


s = input() # считает сумму повторяемых символов и выводит их в строку
encoded = []
count = 1
for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(f"{s[i - 1]}{count}")
            count = 1
# Добавляем последний символ и его счетчик
encoded.append(f"{s[-1]}{count}")

print("".join(encoded))
