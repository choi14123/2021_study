gap = int(input("물건 값을 입력하시오 : ")) # 물건 값 입력

input_coin_1000 = int(input("1000원 지폐개수 : ")) #지불한 돈 입력
input_coin_500 = int(input("500원 동전개수 : "))
input_coin_100 = int(input("100원 동전개수 : "))

input_total = (input_coin_1000 * 1000) + (input_coin_500*500) + (input_coin_100*100) #총 지불한 값

total = input_total - gap # 총 지불한 값에서 물건 값 빼기

# 거스름돈 구하기

coin_500 = (total // 500)

total = total - (coin_500 * 500)

coin_100 = (total // 100)

total = total - (coin_100 * 100)

coin_50 = (total // 50)

total = total - (coin_50 * 50)

coin_10 = (total // 10)

total = total - (coin_10 * 10)

coin_5 = (total // 5)

total = total - (coin_5 * 5)

# 출력문

print("==거스름돈 출력==")
print("500원 = {} , 100원 = {} , 50원 = {} , 10원 = {} , 5원 = {} , 1원 = {} ".format(coin_500,coin_100,coin_50,coin_10,coin_5,total))

