import qrcode

import sys
args = sys.argv

import_file = args[1]

d_txt = open("projects/Python_dmdm/fujimoto/skillup/" + import_file, mode="r", encoding="utf-8")

urls = d_txt.read().splitlines()
num=1

for i in urls:
    img = qrcode.make(i)
    img.save('projects/Python_dmdm/fujimoto/skillup/'+ str(num) +'.png')
    num+=1

d_txt.close()