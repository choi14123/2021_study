import pandas as pd
df = pd.read_csv("/Users/choichanghwan/Desktop/weather.csv", encoding='euc-kr')
#1번.
print(df.head(3))
print(df.tail(3))
#2번.
print(df[df['일시'].isin(['2015-06-06'])])
#3번.
print(df['평균기온'].max())
#4번.
print(df.loc[1103])
#5번.
print(df[ df['평균기온'] >= 30.0])



