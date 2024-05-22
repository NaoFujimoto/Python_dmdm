#入力された整数が素数かどうかを判定する

#魔法の呪文
import sys
args = sys.argv
i = 2

# 入力する整数
number = int(args[1])

#1000以上が入力された場合
if number >= 1000:
    print("1000以上は判定できません",end="")
else:
    #割り切れた場合→素数じゃない
    while i<number:
        if number%i == 0:
            judge = ("not")
            break
        else:
            i+=1
        judge = ("Prime")
    #判定を出す
    print(judge,end="")



