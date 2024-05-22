#魔法の呪文
import sys
args = sys.argv
#データベースのstationsをimportする

# 入力する整数
distance1 = str(args[1])#距離1の駅名
distance2 = str(args[2])#距離2の駅名

#テーブルから入力された数値を呼び出す
#python教材のP95の内容を参考にしつつ記述（.filter_by）
#holidaylist=session.query(Holiday.holi_date)テーブルID、項目IDで項目のみ取得
#.filter_by(holi_text="憲法記念日").all()



#呼び出された数値のdistance1-distance2を引いて絶対値で出力する（例：東京-大阪）
last_distance = distance1-distance2
print(abs(last_distance),end="")
