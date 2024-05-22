#リストを作成
name_list = ["Kurita","Tanaka","Kaneda","Noda","Koyama","Adachi","Kuriyama","Ohyama","Kishida"]

#奇数の要素をいれる空のリスト
odd_list = []
for i in name_list:
    if name_list.index(i)%2 == 1:
        odd_list.append(i)
    else:
        pass

#出力する
print(odd_list,end="")
