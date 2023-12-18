# You are given a list of integers representing the daily stock prices of a company. 
# You can only buy and sell once and you must buy first before you sell. Write a function 
# to find the maximum profit you can make.

# For example, given the list [7, 1, 5, 3, 6, 4], the function should return 5, 
# which is the maximum profit that can be made by buying at a price of 1 and selling 
# at a price of 6.

# Another example, given the list [3, 20, 5, 1, 8, 10], the function should return 17,
# whis is the maximum profit you can get with buying at 3 and selling at 20. Notice that the 
# lowest stock price in this list is 1 but because you have to buy first before you sell you can 
# only sell this stock at a price of either 8 or 10 gaining a max profit of 9. 



def stock_market(alist):
    max_profit = 0
    min_buying_price = float("inf")    
for i in range(0,len(alist)-1):
            buying = alist[i]        
if buying < min_buying_price:
            min_buying_price = buying        
            sell_buy_combo = alist[i] - min_buying_price        
if sell_buy_combo > max_profit:
            max_profit = sell_buy_combo    
            return max_profitprint(stock_market([3, 20, 5, 1, 8, 10]))

def stock_market(alist):
    max_profit = 0    for i in range(0,len(alist)-1):
        for j in range(i, len(alist)):            sell_buy_combo = alist[j] - abs(alist[i])            if sell_buy_combo > max_profit:
                max_profit = sell_buy_combo    return max_profitprint(stock_market([3, 20, 5, 1, 8, 10]))def stock_market(alist):
    max_profit = 0    for i in range(0,len(alist)-1):
        for j in range(i, len(alist)):            sell_buy_combo = alist[j] - abs(alist[i])            if sell_buy_combo > max_profit:
                max_profit = sell_buy_combo    return max_profitprint(stock_market([3, 20, 5, 1, 8, 10]))