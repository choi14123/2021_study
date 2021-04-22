def first_str (): # first_str 함수 정의
    
    #단어 입력 받기
    a = input("첫번째 단어를 입력하여주세요 :") 
    b = input("두번째 단어를 입력하여주세요 :")
    c = input("세번째 단어를 입력하여주세요 :")
    
    #단어 첫번째 글자 대문자로 바꾸면서 저장
    a_ = a[0].upper()
    b_ = b[0].upper()
    c_ = c[0].upper()
    
    print("약자 : {} ({} {} {})".format(a_+ b_ + c_, a , b , c))

first_str()
