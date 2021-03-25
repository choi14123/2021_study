id = "ilovepython"
pa = "mypass1234"

s = input("아이디를 입력하세요 : ")
d = input("패스워드를 입력하세요 : ")

if s == id and d == pa :
    print("환영합니다. ")
elif s != id :
    print("아이디가 틀렸습니다. ")
elif d != pa :
    print("패스워드가 틀렸습니다. ")
