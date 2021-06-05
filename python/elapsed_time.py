import time

# 처리전 시간 취득
t1 = time.time()

# 처리(샘플로 반복문 작성)
for i in range(2,10):
    for n in range(1,10):
        print("{} * {} = {}".format(i, n, i * n))

# 처리후 시간 취득
t2 = time.time()

# 처리시간 계산
elapsed_time = t2-t1

# 경과 시간 출력
print(f"처리시간：{elapsed_time}")
