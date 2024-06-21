def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "除數不能為零！"

print("選擇操作：")
print("1. 加")
print("2. 減")
print("3. 乘")
print("4. 除")

choice = input("輸入你的選擇(1/2/3/4): ")

num1 = float(input("輸入第一個數字: "))
num2 = float(input("輸入第二個數字: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("無效的輸入")
