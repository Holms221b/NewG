# --------------------------------------------КАЛЬКУЛЯТОР
a = float(input())
b = float(input())
c = input()

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/' and b != 0:
    print(a / b)
elif c == '*':
    print(a * b)
elif c == 'mod' and b != 0:
    print(a % b)
elif c == 'pow':
    print(a ** b)
elif c == 'div' and b != 0:
    print(int (a // b))
elif b == 0:
    print("Деление на 0!")


####################################### еще вариант

# try:
#     print (eval((('({0}){2}{1}').format(input(), input(), input())
#                                 .replace('mod','%')
#                                 .replace('pow','**')
#                                 .replace('div','//'))))
# except ZeroDivisionError:
#     print('Деление на 0!')