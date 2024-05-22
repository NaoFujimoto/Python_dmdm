#ランチの売上高、原価、粗利を計算する
#魔法の呪文
import sys
args = sys.argv

# 唐揚げ定食とカレーセットの一日の注文個数を計算
kara_order = int(args[1])
curry_order = int(args[2])

# 売上高を計算
kara_sales = kara_order * 760
curry_sales = curry_order * 850
sales = round(kara_sales + curry_sales)

# 原価を計算
kara_cost = round(kara_sales * 0.323)
curry_cost = round(curry_sales * 0.284)
cost = round(kara_cost + curry_cost)

# 粗利を計算
kara_profit = round(kara_sales - kara_cost)
curry_profit = round(curry_sales - curry_cost)
profit = round(kara_profit + curry_profit)

# 売上高、原価、粗利を出力
print("売上高："+str(sales)+"、"+"原価："+str(cost)+"、"+"粗利："+str(profit),end="")