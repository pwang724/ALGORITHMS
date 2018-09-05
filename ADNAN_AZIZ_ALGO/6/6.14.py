import random as random

def hash_combination(n, k):
    result = []
    dict = {}

    for i in range(0, k):
        rand = random.randint(i, n-1)
        if rand in dict:
            result.append(dict[rand])
        else:
            result.append(rand)

        if i in dict:
            dict[rand] = dict[i]
        else:
            dict[rand] = i

    return result


if __name__ == "__main__":
    print(hash_combination(5,4))