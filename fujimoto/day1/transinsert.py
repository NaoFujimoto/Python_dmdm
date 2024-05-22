from datetime import date
from distance_database import session
from distance_tables import Transport

import sys
args = sys.argv

try:
    #引数→日付の取得
    dt = date(int(args[1][0:4]), int(args[1][4:6]), int(args[1][6:8]))

    ins = Transport(
        date = dt,
        seq = args[2],
        departure = args[3],
        arrival = args[4],
        via = args[5],
        amount = args[6]
    )

    #INSERT処理
    session.add(ins)
    session.commit()

    print("交通費精算テーブルにデータを登録しました")
except :
    print("error:交通費精算テーブルにデータを登録できませんでした")