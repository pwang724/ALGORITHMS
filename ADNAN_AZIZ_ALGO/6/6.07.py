def getprofit(l):
    cur_min = l[0]
    max_profit = 0

    for i in range(1, len(l)):
        cur_profit = l[i] - cur_min
        max_profit = max(max_profit, cur_profit)
        cur_min = min(l[i], cur_min)
    return max_profit

def get_two_profit(l):
    max_profit = 0
    for i in range(2,len(l)-1):
        first_max_profit = getprofit(l[:i])
        second_max_profit = getprofit(l[i:])
        assert(len(l[i:]) > 1)
        cur_profit = first_max_profit + second_max_profit
        max_profit = max(max_profit, cur_profit)
    return max_profit

def get_two_profit_better(l):
    max_profit = 0
    a = []
    cur_min = l[0]
    for i in range(1, len(l)):
        cur_profit = l[i]-cur_min
        max_profit = max(max_profit, cur_profit)
        cur_min = min(l[i],cur_min)
        a.append(max_profit)

    max_profit = 0
    b = []
    cur_max = l[-1]
    for i in reversed(range(0, len(l)-1)):
        cur_profit = cur_max - l[i]
        max_profit = max(max_profit, cur_profit)
        cur_max = max(l[i],cur_max)
        b.insert(0,max_profit)

    c = list(map(lambda x,y: x +y , a,b))

    return max(c)


if __name__ == "__main__":
    l = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    print(get_two_profit_better(l))