from database import session
from table_tra import transport
import sys

args=sys.argv
file_name=args[1]
w_text=session.query(transport).all()
a_file=open("../../files/{0}".format(file_name),mode="w",encoding="utf-8")
for item in w_text:
    a_file.write('"{0}",'.format(str(item.date)))
    a_file.write('"{0}",'.format(str(item.seq)))
    a_file.write('"{0}",'.format(str(item.departure)))
    a_file.write('"{0}",'.format(str(item.arrival)))
    a_file.write('"{0}",'.format(str(item.via)))
    a_file.write('"{0}"'.format(str(item.amount)))
    a_file.write("\n")
a_file.close()