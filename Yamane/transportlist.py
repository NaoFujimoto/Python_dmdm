from database import session
from transporttable import Trains

# データを取得する
transportlist = session.query(Trains).all()

# 取得したデータリストをループで回して表示
for transport in transportlist:
    print(f"日付: {transport.data}, シーケンス: {transport.seq}, 出発地: {transport.departure}, 到着地: {transport.arrival}, 経由: {transport.via}, 金額: {transport.amount}")

