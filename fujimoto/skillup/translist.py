from datetime import date
from distance_database import session
from distance_tables import Transport

import sys
args = sys.argv

export_file = args[1]

d_txt = open("projects/Python_dmdm/fujimoto/skillup/" + export_file, mode="w", encoding="utf-8")
rec=session.query(Transport).all()

for i in rec:
    d_txt.write('"' + str(i.date) + '","' + str(i.seq) + '","' + str(i.departure) + '","' + str(i.arrival) + '","' + str(i.via) + '","' + str(i.amount) + '"\n')

d_txt.close()