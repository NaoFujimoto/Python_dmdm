#【復習】奇数、偶数判定
#魔法の呪文
import sys
args = sys.argv

#入力する整数
number = int(args[1])

#もしinput1が奇数ならばprint→奇数、それ以外ならばprint→(偶数)
if number%2 == 1:
    print("奇数",end="")
else:
    print("偶数",end="")