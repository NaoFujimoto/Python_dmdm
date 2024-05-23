from datetime import date
from distance_database import session
from distance_tables import Stations

# 登録するデータの編集
tokyo= Stations(
    seq = 1,
    name = "東京",
    kilo = 0.00
)

shinagawa= Stations(
    seq = 2,
    name = "品川",
    kilo = 6.78
)

shinyokohama= Stations(
    seq = 3,
    name = "新横浜",
    kilo = 25.54
)

nagoya= Stations(
    seq = 4,
    name = "名古屋",
    kilo = 342.02
)

kyoto= Stations(
    seq = 5,
    name = "京都",
    kilo = 476.31
)

shinosaka= Stations(
    seq = 6,
    name = "新大阪",
    kilo = 515.35
)

#INSERT処理
session.add(tokyo)
session.add(shinagawa)
session.add(shinyokohama)
session.add(nagoya)
session.add(kyoto)
session.add(shinosaka)
#コミット
session.commit()
