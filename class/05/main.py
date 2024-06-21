import calculator

def main():
    print("簡單計算器")
    a = float(input("輸入第一個數字："))
    b = float(input("輸入第二個數字："))

    print(f"{a} + {b} = {calculator.add(a, b)}")
    print(f"{a} - {b} = {calculator.subtract(a, b)}")
    print(f"{a} * {b} = {calculator.multiply(a, b)}")
    print(f"{a} / {b} = {calculator.divide(a, b)}")

if __name__ == "__main__":
    main()
