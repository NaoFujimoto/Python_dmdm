import sys
from database import session
from transporttable import Trains
from datetime import date

# コマンドライン引数からファイル名を取得
txt_file = sys.argv[1]

# Trainsテーブルから全データを取得
transportlist = session.query(Trains).all()

# ファイルパスを正しく組み立てる
file_path = f"C:\\Seminar\\python\\output\\{txt_file}"

with open(file_path, mode="w", encoding="utf-8") as f:
    for transport in transportlist:
        f.write(f"{transport.data}, {transport.seq}, {transport.departure}, {transport.arrival}, {transport.via}\n")
