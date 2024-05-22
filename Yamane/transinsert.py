from datetime import datetime
from database import session
from transporttable import Trains
import sys

args = sys.argv

try:
    # コマンドライン引数から日付とシーケンス番号を取得して変換
    data = datetime.strptime(args[1], '%Y-%m-%d').date()
    seq = int(args[2])
except ValueError as e:
    print(f"入力エラー: {e}")
    sys.exit()

# 既存のレコードがあるか確認
existing_record = session.query(Trains).filter_by(data=data, seq=seq).first()

if existing_record:
    print("error: 交通費精算テーブルにデータを登録できませんでした")
    sys.exit()
else:
    # 新しいレコードを作成して挿入
    expence = Trains(data=data, seq=seq, departure=args[3], arrival=args[4], via=args[5], amount=int(args[6]))
    
    # INSERT処理
    session.add(expence)
    
    # コミット
    session.commit()
    print("交通費精算テーブルにデータを登録しました")

