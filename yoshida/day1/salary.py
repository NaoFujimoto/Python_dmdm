#【復習】給与の支払い額を計算しよう
#魔法の呪文
import sys
args = sys.argv

#入力する整数
salary = int(args[1])

#給与が100万円を超えるならば、100万円を超える部分に税20%をかけて+10万円、それ以外は税10%をかける
if salary > 100:
    salary-100*0.2+100000
else:
    print("偶数",end="")