#! /usr/bin/env python3
import random

# 生成目標數字
target_number = random.randint(1, 100)

# 初始化猜測次數
guesses = 0

print("歡迎來到猜數字遊戲！")
print("我已經選擇了一個介於1和100之間的數字。你能猜出是什麼嗎？")

while True:
    # 獲取玩家的輸入
    guess = int(input("請輸入您的猜測："))

    # 增加猜測次數
    guesses += 1

    if guess < target_number:
        print("太低了！")
    elif guess > target_number:
        print("太高了！")
    else:
        print(f"恭喜你，猜中了！目標數字是{target_number}。您總共猜測了{guesses}次。")
        break
