import sys
from datetime import datetime
from stations_database import session
from stations_tables import Transport

# コマンドライン引数を確認
if len(sys.argv) != 7:
    print("引数の数が正しくありません。")
else:
    # 日付の形式を確認し、Transportオブジェクトを作成
    try:
        transport = Transport(
            date=datetime.strptime(sys.argv[1], '%Y%m%d').date(),
            seq=int(sys.argv[2]),
            departure=sys.argv[3],
            arrival=sys.argv[4],
            via=sys.argv[5],
            amount=int(sys.argv[6])
        )
        # INSERT処理とコミット
        session.add(transport)
        session.commit()
        print("交通費精算テーブルにデータを登録しました")
    except ValueError as e:
        print(f"エラー: {e}")
