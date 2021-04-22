import random # 랜덤 내장함수 
def genPassword():

    n = int(input("몇 개의 패스워드가 필요하신가요?"))

    list = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p',
            'q','r','s','t','u','v','w','x','y','z',0,1,2,3,4,5,6,7,8,9]

    passWord_list = []

    for j in range(0,n):
        for i in range(0,6):
            print(list[random.randrange(1,36)], end ='') # 무작위 비밀번호 생성 후 출력

        print("\n") # 줄 바꿈


genPassword()
