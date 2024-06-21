import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("我已經想好了一個 1 到 100 之間的數字。")
    print(f"你有 {max_attempts} 次機會猜中它。")

    while attempts < max_attempts:
        guess = int(input("請輸入你的猜測："))
        attempts += 1

        if guess < number:
            print("猜小了，再試一次。")
        elif guess > number:
            print("猜大了，再試一次。")
        else:
            print(f"恭喜你！你在第 {attempts} 次猜中了數字 {number}！")
            return

    print(f"很遺憾，你沒能猜中數字。答案是 {number}。")

guess_number()
