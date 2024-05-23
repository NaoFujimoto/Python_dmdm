#ライブラリからインポート
import  sys
from datetime import date
from stations_database import session
from stations_tables import Transport
args = sys.argv

#DBに値を登録
transport = Transport(
    date = int(args[1]),
    seq = int(args[2]),
    departure = args[3],
    arrival = args[4],
    via = args[5],
    amount = int(args[6])
)

#INSERT処理
session.add(transport)

#コミット
session.commit()

#出力
word = "交通費精算テーブルにデータを登録しました"
print(word)