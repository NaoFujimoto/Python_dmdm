#ライブラリからインポート
import  sys
from stations_database import session
from stations_tables import Stations
args = sys.argv

#新幹線駅名（引数）と距離を紐づける
station_name1 = session.query(Stations).filter_by(name=args[1]).first()
station_name2 = session.query(Stations).filter_by(name=args[2]).first()

#距離間の計算
distance = abs(station_name1.kilo- station_name2.kilo)

#出力
print(distance)