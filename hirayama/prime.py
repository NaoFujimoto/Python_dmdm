import sys
args=sys.argv
number=int(args[1])
number_list=[]
i=3
#1000以上は判定できない
if number>=1000:
    print("1000以上は判定できません",end="")
    exit()
#2だった場合素数と判定
elif number ==2:
    print("Prime",end="")
#2以外で偶数だった場合素数と判定
elif number%2==0:
    print("not",end="")
else:
    #奇数で素数か判定する処理
    while True:
        if number % i ==0:
            number_list.append(i)
        i+=2
        if i==number:
            break
    if len(number_list) > 1:
        print("not",end="")
    else:
        print("Prime",end="")


        