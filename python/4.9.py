import random
name1 = input("Player 1의 이름을 입력하세요 : ")
name2 = input("Player 2의 이름을 입력하세요 : ")

name1_score = random.randint(1, 6)
name2_score = random.randint(1, 6)

print(" ........주사위를 굴립니다....... ")
print(name1, "주사위 번호는 :",name1_score)
print(name2, "주사위 번호는 :",name2_score)

if name1_score > name2_score :
    print(name1, "이 이겼습니다! ")
elif name1_score < name2_score :
    print(name2, "이 이겼습니다! ")
else :
    print("비겼습니다! ")
