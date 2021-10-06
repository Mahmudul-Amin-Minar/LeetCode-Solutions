def maxProfit(prices) -> int:

    maximum_profit = 0
    minimum_price = float('inf')

    for price in prices:
        minimum_price = min(price, minimum_price)
        profit = price - minimum_price
        maximum_profit = max(profit, maximum_profit)
    
    return maximum_profit

print(maxProfit([2,4,1]))