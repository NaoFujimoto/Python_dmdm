import sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
args=sys.argv

#唐揚げ定職の個数
kara=int(args[1])
#カレーセットの個数
kare=int(args[2])
#売り上げの計算
sum=kara*760+kare*850
#原価の計算
genka=Decimal(kara*760*0.323+kare*850*0.284).quantize(Decimal('0'), ROUND_HALF_UP)
#粗利の計算
ara=sum-genka
print("売上高：{0}、原価：{1}、粗利：{2}".format(sum,genka,ara),end="")
