a = ['한국','일본','중국','미국','러시아','베트남']

for i in range (6) :
    a_ = input("나라이름을 입력하세요 : ")
    if a_ in a :
        print(a.index(a_))
    else :
        print( str(a_ ) , "is not in list 국가는 리스트에 존재하지 않습니다. 로그기록")
        f = open('/Users/choichanghwan/Desktop/2021_study/python/ErrorLog.txt', 'a')
        f.write(a_)
        f.write("\n")
        f.close()   
     
