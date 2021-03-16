inFp = None
inList, inStr = [], ""

inFp = open("C:/Temp/data1.txt", "r", encoding="UTF8")

inList = inFp.readlines()
for inStr in inList :
    	print(inStr, end="")

inFp.close()
