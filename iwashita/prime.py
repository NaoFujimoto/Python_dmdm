#ライブラリをインポート
import  sys
args = sys.argv

#値を入力
count = int(args[1])
count

#処理（やりたい事：１以外と自分の数字-1までの数字で割れるかどうか　※1000以上は除外）
def is_prime(count):

    # 1 未満の数は素数ではない
    if count < 2:
        return False
    
    #countまでの数について割り切れる数があるか判定
    for i in range(2,count):

        # 割り切れる数がある場合、素数ではない
        if count % i == 0:
            return False
        
    # 割り切れる数がない場合、素数である
    return True

if count >= 1000:
    print("1000以上は判定できない")
elif is_prime(count):
    print("Prime")
else:
    print("not")