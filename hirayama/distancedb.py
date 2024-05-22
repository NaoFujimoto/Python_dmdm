import sys
from database import session
from table import stations
args=sys.argv
basyo1=args[1]
basyo2=args[2]

basyo1=session.query(stations.kilo).filter_by(name=basyo1).first()
basyo2=session.query(stations.kilo).filter_by(name=basyo2).first()

print(round(abs(basyo1.kilo-basyo2.kilo),2),end="")