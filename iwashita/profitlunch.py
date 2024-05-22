#ライブラリをインポート
import  sys
args = sys.argv

#唐揚げとカレーの引数を定義
chicken_count = int(args[1])
curry_count = int(args[2])

#定価を定義
chicken_price = 760
curry_price = 850

#原価率を定義
chicken_costlate = 0.323
curry_costlate = 0.284

#売り上げ計算
chicken_total = chicken_count* chicken_price
curry_total = curry_count* curry_price

#原価計算
ch = chicken_price* chicken_costlate
cu = curry_price* curry_costlate

#原価計算2
chicken_costprice = ch* chicken_count
curry_costprice = cu* curry_count

#売上高合算●
oneday_totalsales = chicken_total+ curry_total

#原価合算●
oneday_totalcostprice = round(chicken_costprice+ curry_costprice)

#粗利計算●
gross_profit = oneday_totalsales- oneday_totalcostprice

#出力
print("売上高：{0}、原価：{1}、粗利：{2}".format(str(oneday_totalsales),str(oneday_totalcostprice),str(gross_profit)),end="")