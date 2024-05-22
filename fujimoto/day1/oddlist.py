namelist = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]

#odd_namelist = []
#
#for i in namelist:
#    if namelist.index(i)%2 ==1:
#        odd_namelist.append(i)
#    else:
#        pass
#
#print(odd_namelist, end="")

l = len(namelist)
print(namelist[1:l:2])