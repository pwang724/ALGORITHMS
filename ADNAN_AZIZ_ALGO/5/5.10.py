import random
import numpy as np
import matplotlib.pyplot as plt

def generate(a, b):
    r = b - a
    p = 0
    while (r > (1 << p)):
        p += 1

    while (True):
        y = 0
        for i in range(0, p):
            x = random.randint(0,1)
            y = y << 1 | x
        if y <= r:
            break

    return a + y

l = []
for i in range(10000):
    l.append(generate(5,10))
x = np.histogram(l, 6)
plt.hist(l, bins = 'auto')
plt.show()