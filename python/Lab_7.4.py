import random
quotes = []
quotes.append("분노는 바보들의 가슴 속에서 살아간다.")
quotes.append("시작이 반이다.")
quotes.append("사람은 사랑할때 누구나 시인이 된다.")
quotes.append("꿈을 지녀라 그러면 어려운 현실을 이겨낼수있다.")
quotes.append("고생없이 얻을 수 있는 진실로 귀중한 것은 없다.")

print('#' * 9)
print('# 오늘의 명언 #')
print('#' * 9)
print("")
dailyQuote =  random.choice(quotes)
print(dailyQuote)
