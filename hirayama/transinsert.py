from database import session
from table_tra import transport
import sys
import datetime

args=sys.argv
date=args[1]
seq=int(args[2])
depa=args[3]
arr=args[4]
via=args[5]
amo=args[6]
count1=session.query(transport.seq).filter_by(seq=seq).count()
count2=session.query(transport.date).filter_by(date=date).count()
if count1 > 0 and count2 > 0:
    print("error:交通費精算テーブルにデータを登録できませんでした")
else:
    date=datetime.datetime.strptime(date,'%Y%m%d')
    date = date.date()
    attend=transport(
        date=date,
        seq=seq,
        departure=depa,
        arrival=arr,
        via=via,
        amount=amo
    )
    session.add(attend)
    session.commit()
