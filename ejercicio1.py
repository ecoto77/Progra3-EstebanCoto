year =input("ingrese un año: ")
if year%100==0:
    print "siglo: " + str(year/100)
else:    
    print "siglo: " + str(year/100)+1
