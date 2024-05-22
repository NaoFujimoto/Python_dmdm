import sys
from sqlalchemy import Column, String, Date, Integer,VARCHAR,DECIMAL
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class Stations(Base):
    __tablename__ = 'stations'
    seq = Column('駅番号', Integer, primary_key = True)
    name = Column('駅名', VARCHAR(20))
    kilo = Column('距離(km)',DECIMAL(6,2))


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)