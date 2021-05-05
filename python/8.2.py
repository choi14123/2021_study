items = { "커피 음료" : 7, "펜" : 3, "종이컵" : 2, "우유" : 1, "콜라" : 4, "책" : 5 }

while True:
    name = int(input("메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료  :"))
    if name == 1:
        num = input("물건의 이름을 입력하세요 :")
        print("재고 :", items[num])
    elif name == 2:
        a, b = input('[입고] 물건의 이름과 수량을 입력하세요 : ').split()
        items[a] = items[a] + int(b)
        print("{}의 재고 :{}".format(a, items[a]))
    elif name == 3:
        a, b = input('[입고] 물건의 이름과 수량을 입력하세요 : ').split()
        items = {"커피 음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}
        items[a] = items[a] - int(b)
        print("{}의 재고 :{}".format(a, items[a]))
    else :
        print("프로그램을 종료합니다.")
        break


