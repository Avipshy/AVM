def maxprofit(prices):
    
    if len(prices) < 2: 
        return 0

    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        current_profit =  prices[i] - min_price

        if current_profit > max_profit:
            max_profit = current_profit
        
        elif prices[i] < min_price:
            min_price = prices[i]

    return max_profit
    
print(maxprofit([7,1,5,3,6,4]))
print(maxprofit([7,6,4,3,1]))


