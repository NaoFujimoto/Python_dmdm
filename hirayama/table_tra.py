import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class transport(Base):
    __tablename__ = 'transport'
    date = Column('date', Date, primary_key = True)
    seq = Column('seq', Integer,primary_key = True)
    departure = Column('departure', String(20))
    arrival = Column('arrival', String(20))
    via = Column('via', String(40))
    amount = Column('amount', Integer)

    
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)