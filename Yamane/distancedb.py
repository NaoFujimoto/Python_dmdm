from database import session
from tables import Stations
import sys
args=sys.argv

station1_data = session.query(Stations).filter_by(name=args[1]).first()
station2_data = session.query(Stations).filter_by(name=args[2]).first()

distance = abs(station1_data.kilo - station2_data.kilo)

print(distance)
