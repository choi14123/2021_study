import matplotlib.pyplot as plt

Dachshund_length = [77,78,85,83,73,77,73,80]
Dachshund_height = [25,28,29,30,21,22,17,35]

Samoyed_length = [75,77,86,86,79,83,83,88]
Samoyed_height = [56,57,50,53,60,53,49,61]

Maltese_length = [34,38,38,41,30,37,41,35]
Maltese_height = [22,25,19,30,21,24,28,18]

plt.title("Dog size")
plt.ylabel("Height")
plt.xlabel("Length")

plt.scatter(Dachshund_length, Dachshund_height, c = "red", marker = "o", label = "Dachshund")
plt.scatter(Samoyed_length, Samoyed_height, c = "blue", marker = "^", label = "Samoyed")
plt.scatter(Maltese_length, Maltese_height, c = "green", marker = "s", label = "Maltese")

plt.legend()
plt.show()
