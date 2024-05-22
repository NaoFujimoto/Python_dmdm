import sys
args=sys.argv

#唐揚げ定職の個数
kara=int(args[1])
#カレーセットの個数
kare=int(args[2])

print(kara*760+kare*850,end="")