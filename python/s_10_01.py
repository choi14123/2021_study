import numpy as np

players = np.zeros((100,3))
mu = 175
sigma = 10
players = mu + sigma * np.random.randn(100,1)
mu1 = 70
sigma1 = 10
players1 = mu1 + sigma1 * np.random.randn(100,1)
mu2 = 22
sigma2 = 10
players2 = mu2 + sigma2 * np.random.randn(100,1)

a = np.array(players)
a1 = np.array(players1)
a2 = np.floor(np.array(players2))

b = np.median(players)
b1 = np.median(players1)
b2 = np.floor(np.median(players2))

print("신장 평균값 : {}" .format(a.mean()))
print("신장 중앙값 : {}" .format(b))
print("체중 평균값 : {}" .format(a1.mean()))
print("체중 중앙값 : {}" .format(b1))
print("나이 평균값 : {: 2}" .format(a2.mean()))
print("나이이중앙값 : {: 2}" .format(b2))
