coin = {"10000":0, "5000":0, "1000":0, "500":0, "100":0, "50":0, "10":0}
vending = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}

'''
１．10000円を超える金額は購入できない
２．入力された金額では何も買えない（100円未満）
３．1円玉と5円玉は投入できない（10で割ると余りがでる）
'''

have = 0

def change(num):
    #おつり出すよ
    print("おつり\n")
    for i in coin.items():
        while num != 0:
            if num-int(i[0])>=0:
                num -= int(i[0])
                coin[i[0]] += 1
            else:
                break
    for j in coin.items():
        if int(j[0])%1000==0 and int(j[1])>0:
            print(str(j[0]) + "円札：" + str(j[1]) + "枚")
        elif int(j[0])%1000!=0 and int(j[1])>0:
            print(str(j[0]) + "円玉：" + str(j[1]) + "枚")

while True:
    if have==0:
        for key, value in vending.items():
            print(str(key) + "：" + str(value) + "円\n")
        #投入金額入力
        invest = int(input("投入金額を入力してください"))
    elif have!=0:
        for key, value in vending.items():
            print(str(key) + "：" + str(value) + "円\n")

    if invest<=10000 and invest >= 100 and invest%10==0:
        #何を購入するか聞く
        which_buy =str(input("何を購入しますか（商品名/cansel）"))
        #選択したものが商品の中にある and 選択したものを買える投入金額である
        if which_buy in vending and invest >= int(vending[which_buy]):
            #所持金から購入分の金額を引く
            invest -= int(vending[which_buy])
            #まだ買えるものがある場合
            if invest >= 100:
                #残金表示
                print("残金：" +str(invest)+ "円\n")
                #続けて購入するか尋ねる
                nextbuy = input("続けて購入しますか（Y/N）")
                #もうこないからね～🫠
                if nextbuy == "N":
                    change(invest)
                    break
                #お買い物をつづける
                elif nextbuy == "Y":
                    have = 1;
                    continue
            elif invest != 0 and invest < 100:
                change(invest)
                break
            elif invest == 0:
                break
        elif which_buy=="cansel":
            change(invest)
            break
        elif which_buy not in vending and which_buy!="cansel":
            print("その商品はありません\n")
            continue
        elif invest < int(vending[which_buy]):
            print("お金が足りません\n")
            continue
    elif invest>10000:
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください\n")
        continue
    elif invest<100:
        print(str(invest) + "円では購入できる商品がありません。再度投入金額を入力してください\n")
        continue
    elif invest%10!=0:
        print("1円玉、5円玉は使用できません。再度投入金額を入力してください\n")
        continue
