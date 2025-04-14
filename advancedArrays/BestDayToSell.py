

# best day to sell stock

prices= [7,1,5,3,6,4]

max_profit = 0  #1
min_price = prices[0] # bying price

for i in range(1,len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
    else:
        max_profit = max(max_profit,prices[i]-min_price)
print(max_profit)


