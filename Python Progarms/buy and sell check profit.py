costPrice = int(input("costPrice : "))
sellPrice = int(input("sellPrice : "))

maxProfit = sellPrice - costPrice

if(maxProfit>0):
    print("Profit", maxProfit)
elif(maxProfit<0):
    print("loss", maxProfit)
else:
    print("no loss no profit")

# o/p :
#     costPrice : 5
#     sellPrice : 7
#     profit 2
#     loss -2
#     no loss no profit 0