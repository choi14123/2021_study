str = input("")
words = str.split(" ")
words = [w for w in words if w != ""]
print(len(words)) 