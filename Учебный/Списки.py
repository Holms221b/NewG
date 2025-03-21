# students = ["Ivan","Masha","Dima"]
# for student in students:
#     print("Hello, " + student + "!")
# from itertools import count

# students = ['Ivan', 'Masha', 'Sasha',1]
# a = len(students) - 1
# students[1] = "Вместо"
# # students += ['Olga']
# # students += 'Olga'
# print(students[::-1])

# students = ["Adf","C","Bsdf"]
# students.sort()
# print(students)

# i = int(input())
# a = [int(i) for i in input().split()] # преобразуем из строки целые числа и суммируем их, где инпут читает и сплит разделяет пробелом, int преобразует в число
# print(sum(a))



# numbers = [int(i) for i in input().split()] # программа вычисляет сумму соседей для каждого элемента списка, учитывая цикличность.
# if len(numbers) == 1:
#     print(numbers[0])
# else:
#     for i in range(len(numbers)):
#         print(numbers[i - 1] + numbers[(i + 1) % len(numbers)], end=" ")

# a=[int(i) for i in input().split()]
# if len(a)>1:
#     for i in range(len(a)):
#         print(a[i-1]+a[i+1-len(a)], end=" ") # предыдущий потом следующий с конца строки - len
# else:
#     print(a[0])

# n = [int(i) for i in input().split()] ###принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
# res = set()
# for i in range(len(n)):
#     for x in range(i+1,len(n)):
#         if n[i] == n[x]:
#             res.add(n[i])
#             break
# print(*res, sep=" ")


# set(a) - дает уникальные значения (без повторов)
# перебираем уникальные значения и удаляем их из входного списка
# итого у нас остаются только дубли во входном списке
# снова берем set(a) и выводим его

# a=input().split()
# [a.remove(i) for i in set(a)]
# print(*set(a))


# a = sorted([int(i) for i in input().split()])
# box = ''
# for i in range(len(a)):
#     if a[i] == a[i-1] and a[i] != box and len (a) > 1:
#         print(a[i],end=' ')
#         box = a[i]
#
b = [int(i) for i in input().split()]

m = b[0] #первое значение
for x in b: #все значения списка
    if m > x: #если текущее значение элемента больше очередное значение
        m = x #обновляем
print(m)