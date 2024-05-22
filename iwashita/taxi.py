import sys
import math
args = sys.argv

# 乗車距離を入力
jyousya_kyori = int(args[1])

# 金額を定義
hatunori_kyori = 1500

# 処理
if jyousya_kyori > hatunori_kyori:
    output = jyousya_kyori- hatunori_kyori
    output = math.ceil(output/344)
    output = output* 98
    output = 630+ output
else:
    output = 630

# 結果を整数に切り上げ
print(output)