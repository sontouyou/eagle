def maxProfit(prices: list[int]) -> int:
    price = 0
    lenprices = len(prices)
    if lenprices < 2:
        return price
    reprices = list(reversed(prices))
    maxitem = max(enumerate(reprices), key=lambda x: x[1])
    maxindex = lenprices - 1 - maxitem[0]
    maxvalue = maxitem[1]
    endindex = lenprices - 1
    while True:
        minitem = min(enumerate(prices[0:endindex+1]), key=lambda x: x[1])
        minindex = minitem[0]
        minvalue = minitem[1]
        if minindex <= maxindex:
            if price < maxvalue - minvalue:
                price = maxvalue - minvalue
            break
        if minindex != endindex:
            tmaxvalue = max(prices[minindex+1:endindex+1])
            if price < tmaxvalue - minvalue:
                price = tmaxvalue - minvalue
        endindex = minindex - 1
        if endindex == 0:
            break
    return price

a = [3,2,1]
print(maxProfit(a))











