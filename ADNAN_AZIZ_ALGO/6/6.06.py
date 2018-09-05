def getprofit_dumb(l):
    maxprofit = 0
    for i in range(len(l) - 1):
        bestprofit = max(l[i+1:]) - l[i]
        maxprofit = max(maxprofit, bestprofit)
    return maxprofit

def getprofit(l):
    cur_min = l[0]
    max_profit = 0

    for i in range(1, len(l)):
        cur_profit = l[i] - cur_min
        max_profit = max(max_profit, cur_profit)
        cur_min = min(l[i], cur_min)
    return max_profit

if __name__ == "__main__":
    l = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    print(getprofit(l))