import random

answer = random.randint(1, 100)
count = 0

print("1から100までの数字を当ててください。")

while True:
    guess = int(input("入力してください: "))
    count += 1

    if guess > answer:
        print("もっと小さい数字です")

    elif guess < answer:
        print("もっと大きい数字です")

    else:
        print(f"正解！ {count} 回で当てました")
        break