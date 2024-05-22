import sys
args=sys.argv
fried_chicken=760*int(args[1])
curry_price=850*int(args[2])

sales=fried_chicken+curry_price
prime_cost=round(fried_chicken*0.323)+round(curry_price*0.284)
gross_profit=sales-prime_cost

print("売上高："+str(sales)+"、"+"原価："+str(prime_cost)+"、"+"粗利："+str(gross_profit),end="")
