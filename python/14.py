import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(10, 3))

x = np.random.normal(25, 6,(1000))
y = np.random.normal(25, 6,(1000))

x1 = np.random.normal(25, 6,(1000))
y1 = np.random.normal(25, 3,(1000))


ax[0].scatter(x, y, color = "blue")
ax[1].scatter(x1, y1, color = "red")

plt.show()
