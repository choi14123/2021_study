inFp = None
inList = ""




inFp = open("/Users/choichanghwan/Desktop/2021_study/python/f1.txt" , "r", encoding = "UTF8")


inList = inFp.readlines()

inList = list(map(int, inList))

hap = sum(inList)
average = hap / len(inList)
inFp.close()


print("전체 합은 ", hap , "입니다. ")
print("전체 평균은 ", int(average) , "입니다. ")


