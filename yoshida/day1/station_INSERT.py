
from database import session
from tables import stations
 
# 入力したいデータベースのリストを作成
stations_list = [
    {"seq":1, "name": "東京","kilo":0.00},
    {"seq":2, "name": "品川","kilo":6.78},
    {"seq":3, "name": "新横浜","kilo":25.54},
    {"seq":4, "name": "名古屋","kilo":342.02},
    {"seq":5, "name": "京都","kilo":476.31},
    {"seq":6, "name": "新大阪","kilo":515.35}
    
    # 他の祝日も同様に追加
]
 
# リスト内の各データに対してHolidayオブジェクトを作成し、データベースに追加
for station in stations_list:
    station_insert = stations(**station)
    session.add(station_insert)
 
# データベースへの変更をコミット
session.commit()
