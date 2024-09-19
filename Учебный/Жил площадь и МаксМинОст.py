# m = input()                                        ####### вычислять жилплощадь
# if ("треугольник") == m:
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     print((a + b + c) / 2)
# elif ("прямоугольник") == m:
#     a = int(input())
#     b = int(input())
#     print ( a * b)
# elif("круг") == m:
#     r = int(input())
#     print( float(3.14 * r ** 2))
                                   ################################### Макс мин и оставшееся число

num = [int(input()), int(input()), int(input())]
s = num.index(max(num))
m = num.index(min(num))
print(max(num))
print(min(num))
if s == 0 and m == 1 or s == 1 and m == 0:
    print(num[2])
elif s == 2 and m == 1 or s == 1 and m == 2:
    print(num[0])
elif s == 2 and m == 0 or s == 0 and m == 2:
    print(num[1])

                                 ################################### Макс мин и оставшееся число

a = int(input())
b = int(input())
c = int(input())

if a <= b <= c:
    print(c,a,b, sep = '\n')
elif b <= a <= c:
    print(c,b,a, sep = '\n')
elif c <= a <= b:
    print(b,c,a,sep = '\n')
elif a <= c <= b:
    print(b,a,c,sep = '\n')
elif b <= c <= a:
    print(a,b,c,sep = '\n')
elif c <= b <= a:
    print(a,c,b,sep = '\n')

                                 ################################### Макс мин и оставшееся число

# x = sorted([int(input()),int(input()),int(input())])
# print (x[1],x[2],x[0], sep="\n")
