a = input()
t = (int(a[0]) + int(a[1]) + int(a[2]))
g = (int(a[3]) + int(a[4]) + int(a[5]))

if  len(a) == 6 and  t == g:
    print("Счастливый")
else:
    print("Обычный")
