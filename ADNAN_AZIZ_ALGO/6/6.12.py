import random as random

def online_combination(List, k):
    current = List[:k]

    for i in range(k, len(List)):
        swap_probability = k / (i+1)
        if random.uniform(0,1) < swap_probability:
            swap_index = random.randint(0, k-1)
            current[swap_index] = List[i]
    return current

if __name__ == "__main__":
    List = ['a','b','c','d','e','f']
    k = 4
    print(online_combination(List, k))


