f = open("idsadmunb.txt","r")
idsadmunb = f.readlines()
f.close()

f = open("idsbceunb.txt","r")
idsbceunb = f.readlines()
f.close()

f = open("idsCACOMUnB.txt","r")
idsCACOMUnB = f.readlines()
f.close()

f = open("idscaecoUnB.txt","r")
idscaecoUnB = f.readlines()
f.close()

f = open("idsCAEnfFCE.txt","r")
idsCAEnfFCE = f.readlines()
f.close()

f = open("idscafarunb.txt","r")
idscafarunb = f.readlines()
f.close()

f = open("idscahisunb.txt","r")
idscahisunb = f.readlines()
f.close()

f = open("idscamu_unb.txt","r")
idscamu_unb = f.readlines()
f.close()

f = open("idsCAREL_UnB.txt","r")
idsCAREL_UnB = f.readlines()
f.close()

f = open("idsCaTur_Unb.txt","r")
idsCaTur_Unb = f.readlines()
f.close()

f = open("idscead_unb.txt","r")
idscead_unb = f.readlines()
f.close()

f = open("idsdceunb.txt","r")
idsdceunb = f.readlines()
f.close()

f = open("idsdeclaracoesunb.txt","r")
idsdeclaracoesunb = f.readlines()
f.close()

f = open("idseditoraunb.txt","r")
idseditoraunb = f.readlines()
f.close()

f = open("idsHermeticaUnB.txt","r")
idsHermeticaUnB = f.readlines()
f.close()

f = open("idsieeecsunb.txt","r")
idsieeecsunb = f.readlines()
f.close()

f = open("idspupilaav.txt","r")
idspupilaav = f.readlines()
f.close()

f = open("idsspottedvsfunb.txt","r")
idsspottedvsfunb = f.readlines()
f.close()

f = open("idsunb_tv.txt","r")
idsunb_tv = f.readlines()
f.close()

f = open("idsUnBdaDepre.txt","r")
idsUnBdaDepre = f.readlines()
f.close()

f = open("idsUnBemes.txt","r")
idsUnBemes = f.readlines()
f.close()

f = open("idsUnBnaCampus.txt","r")
idsUnBnaCampus = f.readlines()
f.close()

f = open("idsunboficial.txt","r")
idsunboficial = f.readlines()
f.close()

ids_total = list(set(idsadmunb+idsbceunb+idsCACOMUnB+idscaecoUnB+idsCAEnfFCE+idscafarunb+idscahisunb+idscamu_unb+idsCAREL_UnB+idsCaTur_Unb+idscead_unb+idsdceunb+idsdeclaracoesunb+idseditoraunb+idsHermeticaUnB+idsieeecsunb+idspupilaav+idsspottedvsfunb+idsunb_tv+idsUnBdaDepre+idsUnBemes+idsUnBnaCampus+idsunboficial))


print (len(ids_total))