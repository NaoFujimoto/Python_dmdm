import sys
args=sys.argv
kyori=int(args[1])
sum=0
if kyori >= 1500 :
    num=kyori/1500
    sum=630
    kyori=kyori-1500
num=kyori/344
sum=sum+98*int(num)
if kyori % 344 !=0:
    sum+=98
    
print(sum,end="")