birth = {"홍길동":"2000년 3월 1일", "김춘추":"604", "김유신":"595년"}
a = ""

while a!='q':
    a = input("생일을 알고 싶은 사람을 입력하세요 : ")
    try:
        print(birth[a])
    except KeyError:
        print("데이터베이스에 존재하지 않는 이름입니다.")
