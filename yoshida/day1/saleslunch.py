#売上高を計算する
#魔法の呪文
import sys
args = sys.argv


input1 = int(args[1])
input2 = int(args[2])

karaage = input1*760
curry = input2*850

sum = karaage+curry

print(sum,end="")
