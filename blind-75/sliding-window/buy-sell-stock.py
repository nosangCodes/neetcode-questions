def buySellStockBrute(prices: list[int]):
    maxProfit = 0
    
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] > prices[i]:
                maxProfit = max(maxProfit, prices[j] - prices[i])
    
    return maxProfit

# print(buySellStockBrute([7,1,5,3,6,4]))
# print(buySellStockBrute([7,6,4,3,1]))


def buySellStock(prices: list[int]):
    maxProfit = 0
    if len(prices) < 2: return maxProfit
    buy = 0
    sell = 1
    
    while sell < len(prices):
        if prices[sell] > prices[buy]:
            maxProfit = max(maxProfit, prices[sell] - prices[buy])
        else:
            buy = sell
        sell+=1
    
    return maxProfit    

print(buySellStock([7,1,5,3,6,4]))
print(buySellStock([7,6,4,3,1]))