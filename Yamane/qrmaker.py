import sys
import os
import qrcode 
 
args=sys.argv
#URLが記載されているファイルを引数で受け取る
file_pass=args[1]
#生成するpingファイル名の初期値
i=1

#URLが記載されているファイルを操作
with open(file_pass,mode="r",encoding="utf-8") as tf:
    #URLがある数分のループ
    for line in enumerate(tf):#enumerateで要素番号と要素
        print(line[1])#一つ目のURLを表示
        img=qrcode.make(line[1])#1つ目のURLのQRコードを生成
        #outputフォルダーに"i".pngのファイルを挿入
        path = os.path.join("../../output","{0}.png".format(i))
        img.save(path)#ファイル保存
        i+=1
 