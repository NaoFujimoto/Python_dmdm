import sys
args = sys.argv

#距離読み込み
distance=int(args[1])

#距離と料金計算
#1500mに収まるときは630円
if distance <=1500:
    fare = 630
else:
    #1500mから何m超過したかを計算する
    extra_distance = distance -1500
    #料金が加算される距離（344m）に達した回数のカウンタ
    extra_fare_count = 1

    #344m（加算1回分）よりも大きい時はさらに344mごとにカウンタを回す
    while extra_distance >344:
        #前の距離から344m（加算1回分）を引く
        extra_distance-=344
        #カウンタを足す
        extra_fare_count+=1

    #超過した際の料金計算
    #~1500mまでの運賃（630円）+超過回数分（超過回数*98円）
    fare = 630 + extra_fare_count*98

#出力
print(fare, end="")