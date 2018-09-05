import random as random

def draw_permutation(List):
    n = len(List)
    for i in range(n):
        idx = random.randint(i,n-1)
        List[idx], List[i] = List[i], List[idx]
    return List

if __name__ == "__main__":
    List = ['a','b','c']
    print(draw_permutation(List))


