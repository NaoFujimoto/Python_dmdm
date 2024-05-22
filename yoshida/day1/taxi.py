#タクシー料金を計算する
#魔法の呪文
import sys
args = sys.argv

#入力
distance = int(args[1])#乗車距離


#1500m以上なら344mごとに＋98円＆1500m分の630円を足す
if distance > 1500:
    a = distance-1500 
    c = 1#ワンカウント
    while a > 344:#この条件を満たす限り繰り返す
        c+= 1
        a-=344#引ける限り距離がある
    sum = 630+c*98
else:
    sum = 630

#出力
print(sum,end="")