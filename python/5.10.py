import random

tries = 0
guess = 0
answer = random.randint(1, 100)

print("1부터 100사이의 수를 입력하세요 ")
while guess != answer:
    guess = int(input("숫자를 입력하세요 :"))
    tries = tries + 1
    if tries == 10 :
        break
    elif guess < answer :
        print("낮음!")
    elif guess > answer :
        print("높음!")

print("축하합니다. 총 시도 횟수=", tries)
