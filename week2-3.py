num1 = int(input("first number: "))
num2 = int(input("second number: "))
flag = False

while num1 > 0:
    if num1 >= num2:
        num1 -= num2
        print(num1)
    elif num1 <= num2:
        print(num1)
        num1 = 0
    else:
        print(num1)
        num1 = 0