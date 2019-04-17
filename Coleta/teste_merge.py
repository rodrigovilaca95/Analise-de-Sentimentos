f = open("idsunboficial.txt","r")
idsunboficial = f.readlines()
f.close()

f = open("idsadmunb.txt","r")
idsadmunb = f.readlines()
f.close()

f = open("idsbceunb.txt","r")
idsbceunb = f.readlines()
f.close()

f = open("idsCACOMUnB.txt","r")
idsCACOMUnB = f.readlines()
f.close()

print (len(idsunboficial))
print (len(idsadmunb))
print (len(idsbceunb))
print (len(idsCACOMUnB))

ids_total = list(set(idsunboficial+idsadmunb+idsbceunb+idsCACOMUnB))
print (len(ids_total))