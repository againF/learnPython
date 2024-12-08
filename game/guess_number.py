import random
def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("欢迎来到猜数字游戏")
    print("请猜一个1-100之间的数字")

    while True:
        try:
            guess = int(input("请输入你的猜测："))
            attempts += 1
            if guess < number_to_guess:
                print("猜的数字太小了，请再试一次")
            elif guess > number_to_guess:
                print("猜的数字太大了，请再试一次")
            else:
                print(f"恭喜你，猜对了！你用了{attempts}次尝试")
                break
        except ValueError:
            print("请输入一个有效的整数")


guess_number()