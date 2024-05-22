import sys
from sqlalchemy import Column, String, Date, Integer,VARCHAR,DECIMAL
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class Trains(Base):
    __tablename__ = 'transport'
    data = Column('利用日',Date,primary_key = True)
    seq = Column('連番', Integer, primary_key = True)
    departure = Column('出発日',VARCHAR(20))
    arrival = Column('到着地',VARCHAR(20))
    via = Column('利用交通機関',VARCHAR(40))
    amount = Column('金額',Integer)


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)