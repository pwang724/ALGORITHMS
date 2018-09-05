# extra, not in problem
def permute_list(real_list):
    def permute(l):
        result = []
        def helper(before, to_permute):
            if not to_permute:
                result.append(before)
            else:
                for i in range(len(to_permute)):
                    new_before = list(before + [to_permute[i]])
                    new_permute = to_permute[0:i] + to_permute[i+1:]
                    helper(new_before, new_permute)
        helper([],list(range(l)))
        return result

    out = []
    result = permute(len(real_list))
    for ordering in result:
        T = map(lambda i: real_list[i], ordering)
        out.insert(0, T)
    return result, out

#
def permute_given_index(List, index):
    for i, idx in enumerate(index):
        if i != idx:
            List[idx], List[i] = List[i], List[idx]
            index[idx], index[i] = index[i], index[idx]
    return List



if __name__ == "__main__":
    l = ['a','b','c','d']
    ordering = [2, 0, 1, 3]
    out = permute_given_index(l, ordering)

    ordering, out = permute_list(l)
    print(ordering)