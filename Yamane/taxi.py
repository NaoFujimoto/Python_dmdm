import sys
import math
args=sys.argv
num=int(args[1])
if num<=1500 :
    print(630)

else :
    num-=1500
    num=math.ceil(num/344)
    num*=98
    print(630+num,end="")
