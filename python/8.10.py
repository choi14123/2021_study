def get_divisors(x, y):
    a = set()
    b = set()
    for i in range(2, y):
        if y % i == 0:
            b.add(i)
    for i in range(2, x):
        if x % i == 0:
            a.add(i)
    print(x, y, "의 최대공약수 : ", max(a.intersection(b)))
    return a, b

x = int(input("첫번째 숫자를 입력하여주세요 : "))
y = int(input("두번째 숫자를 입력하여주세요 : "))
get_divisors(x,y)
