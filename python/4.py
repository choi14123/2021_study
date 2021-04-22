def is_sosu(n):
  if(n<2): # 받은 값이 2보다 작을 경우
    return False # 소수가 아님을 반환

  for i in range(2,n): #2~n 까지. 그 수가 소수인지 아닌지 판별

    if(n%i==0):
      return False# 만약 소수가 아니라면 false 반환
  return True


def is_prime():
    n = 100
    for i in range(n+1):
      if(is_sosu(i)):
        print(i)


is_prime()