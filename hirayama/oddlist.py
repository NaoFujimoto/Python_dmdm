name_list=["Kurita","Tanaka","Kaneda","Noda","Koyama","Adachi","Kuriyama","Ohyama","Kishida"]

#リストのサイズを取得
size=len(name_list)
#出力する名前を格納するリストを初期化
print_list=[]

#添え字が奇数の要素をprint_listに格納
for i in range(size):
    if i%2!=0:
        print_list.append(name_list[i])

print(print_list,end="")