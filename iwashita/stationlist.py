from stations_database import session
from stations_tables import Stations

#データ取得
stations_list = session.query(Stations).all()

for stations in stations_list:
    print(stations.seq,stations.name,stations.kilo)
