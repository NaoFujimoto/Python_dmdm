import sys
args=sys.argv
num = int(args[1])

if num>=1000:
    print ("1000以上は判定できません",end="")
    sys.exit()

if num == 2:
    print("prime", end="")
    sys.exit()

for i in range(2,num) :
    if num%i==0:
        print("not",end="")
        break

    elif i+1==num:
        print("prime",end="")

