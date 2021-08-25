def countHighlyProfitableMonths(stockPrices, k):
 
    # get the number of days`n`
n = len(price)
 
    #`profit[i][j]` stores the maximum profit gained by doing
    # at most`i` transactions till j'th day
profit = [[None for x in range(n)]for y in range(k + 1)]
 
    # fill`profit[][]` matrix in a bottom - up fashion
for i in range(k + 1):
    for j in range(n):
            # profit is 0 when
            #`i = 0`, i.e., for 0th day
            #`j = 0`, i.e., no transaction is being performed

if i == 0 or j == 0:
profit[i][j] = 0
            else:
max_so_far = 0
for x in range(j):
    curr_price = stockPrices[j] - stockPrices[x] + profit[i - 1][x]
if max_so_far < curr_price:
    max_so_far = curr_price

profit[i][j] = max(profit[i][j - 1], max_so_far)

return profit[k][n - 1]