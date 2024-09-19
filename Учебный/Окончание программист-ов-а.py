

# num = input()
# prog = ["программистов","программист","программиста"]
#
# if len(num) > 1 and  num[-2] == "1" or num[-1] == "0" or "5" <= num[-1] <= "9":
#      print(f"{num} {prog[0]}")
# elif num[-1] == "1":
#      print(f"{num} {prog[1]}")
# elif "2"<=num[-1]<="4":
#      print(f"{num} {prog[2]}")

###################           решение при помощи метода строки .endswith()

# num = input()
# ov = ('0', '11', '12', '13', '14', '5', '6', '7', '8', '9')
# ta = ('2', '3', '4')
# if num.endswith(ov):
#     print(num + " программистов")
# elif num.endswith('1'):
#     print(num + " программист")
# elif num.endswith(ta):
#     print(num + " программиста")

