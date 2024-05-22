import sys
args = sys.argv

num = int(args[1])

i = 2
pf = []

if num<1000:
    while num != 1:
        if num%i ==0:
            pf.append(i)
            num/=i
        else:
            i+=1

    if len(pf)+1==2:
        print("Prime",end="")
    elif len(pf)+1!=2:
        print("not",end="")
else:
    print("1000以上は判定できません",end="")