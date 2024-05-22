import datetime
from database import session
from table import stations
import sys

args=sys.argv
name1=args[1]
kilo1=float(args[2])
count=session.query(stations.seq).count()
attend=stations(
    seq=count+1,
    name=name1,
    kilo=kilo1
)
session.add(attend)
session.commit()