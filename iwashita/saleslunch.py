#ライブラリをインポート
import  sys
args = sys.argv

#唐揚げとカレーの引数を定義
chicken_count = int(args[1])
curry_count = int(args[2])

#値段を定義
chicken_price = 760
curry_price = 850

#計算
chicken_total = chicken_count* chicken_price
curry_total = curry_count* curry_price

#合算
oneday_total = chicken_total+ curry_total

print(oneday_total)