import sys
import os
import qrcode

args=sys.argv
file_pass=args[1]
i=1
file_name="hirayama.png"
with open(file_pass,mode="r",encoding="utf-8") as tf:
    for line in enumerate(tf):
        print(line[1])
        img=qrcode.make(line[1])
        path = os.path.join("../../output","{0}.png".format(i))
        img.save(path)
        i+=1
