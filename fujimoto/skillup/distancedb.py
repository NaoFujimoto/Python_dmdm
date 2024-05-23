from datetime import date
from distance_database import session
from distance_tables import Stations

import sys
args = sys.argv

start = str(args[1])
goal = str(args[2])

# データを取得する
s=session.query(Stations).filter_by(name=start).first()
g=session.query(Stations).filter_by(name=goal).first()
print(s)

d = abs(g.kilo-s.kilo)
print(round(d,2), end="")