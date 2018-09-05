
def main(l):
    result = [0]
    states = set()
    def helper(l, idx):
        if idx not in states:
            states.add(idx)

        if idx == len(l) - 1:
            result[0] = 1

        moves = l[idx]
        possible_moves = range(1, moves+1)

        for move in possible_moves:
            nextstate = idx + move
            if nextstate not in states:
                print(idx, nextstate)
                helper(l, nextstate)

    helper(l, 0)
    return result[0]


if __name__ == "__main__":
    l = [3, 2, 0, 2, 2, 0, 0]
    print(main(l))