money = int(input("투입한 돈 : "))
stuff = int(input("물건 값 : "))
change = int(input("거스름돈 : "))
x = change // 500
y = (change - 500 * x) // 100
print("500원 동전의 개수 : " , x)
print("100원 동전의 개수 : " , y)
