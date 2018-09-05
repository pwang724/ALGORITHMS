import random as random

def draw_combination(List, k):
    n = len(List)-1
    for i in range(k):
        idx = random.randint(i,n)
        List[idx], List[i] = List[i], List[idx]
    return List[:k]

if __name__ == "__main__":
    List = ['a','b','c','d','e','f']
    k = 4
    print(draw_combination(List, k))


