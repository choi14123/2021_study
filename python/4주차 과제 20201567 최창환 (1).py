
# 4주차 과제 20201567 최창환

#문제 1.

a = [3, 5, 8, 2, 7, 9, 6, 1, 0, 4]

print("shift 전",a)
for i in range(1, 11) :
    a.append(a[0])
    del a[0]
    print(i,"번째 :",a)



# 문제 2.

a = [] 
b = []

        
for i in range(50) :
    number = int(input("정수(음수 또는 양수를 입력하세요(종료값 : 0)"))
    if number > 0 :
        a.append(number)
    elif number < 0 :
        b.append(number)
    
    else :
        break


print("양의 리스트 =",a)
print("양의 리스트 개수 =",len(a))
print("양의 리스트 합 =",sum(a))
print("양의 리스트 평균 =",round(sum(a) / len(a),2))

print("")

print("음의 리스트 =",b)
print("음의 리스트 개수 =",len(b))
print("음의 리스트 합 =",sum(b))
print("음의 리스트 평균 =",round(sum(b) / len(b),2))
