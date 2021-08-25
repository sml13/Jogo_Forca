def countHighlyProfitableMonths(stockPrices, k)::
 
    n = len(stockPrices)
    profit = [[None for x in range(n + 1)] for y in range(k + 1)]
    for i in range(k + 1):

        prev_diff = -sys.maxsize
 
        for j in range(n):
 
            if i == 0 or j == 0:
                profit[i][j] = 0
            else:
                prev_diff = max(prev_diff, profit[i - 1][j - 1] - stockPrices[j - 1])
                profit[i][j] = max(profit[i][j - 1], stockPrices[j] + prev_diff)
 
    return profit[k][n - 1]