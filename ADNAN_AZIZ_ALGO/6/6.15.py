import random as random
import matplotlib.pyplot as plt

def sample(n_list, p_list):
    cumsum = p_list[:]
    for i in range(1, len(p_list)):
        cumsum[i] += cumsum[i-1]
    cumsum.append(1.1)

    rand = random.uniform(0,1)

    idx = 0
    while (cumsum[idx] < rand):
        idx += 1

    return n_list[idx]

if __name__ == "__main__":
    n_list = [0, 1, 2, 3, 4]
    p_list = [.2, .2, .2, .2, .2]
    l = []

    for i in range(1000):
        l.append(sample(n_list, p_list))
    print(l)
    # plt.hist(l, bins='auto')
    # plt.show()