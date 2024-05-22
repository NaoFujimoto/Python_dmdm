import sys
args = sys.argv

#各売り上げ
karaage_sales = int(args[1])*760
curry_sales = int(args[2])*850

#売り上げ合計
sales = karaage_sales + curry_sales

#原価
karaage_cost = round(karaage_sales*0.323)
curry_cost = round(curry_sales*0.284)

costs = karaage_cost + curry_cost

#粗利
karaage_profit = karaage_sales-karaage_cost
curry_profit = curry_sales-curry_cost

profits = karaage_profit + curry_profit

print("売上高：" +str(sales)+ "、原価：" +str(costs)+ "、粗利：" +str(profits),end="")