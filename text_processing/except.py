try:
   open("a_30000.txt","r")
except IOError:
    print("file cannot open")
else:
   print("okay")

