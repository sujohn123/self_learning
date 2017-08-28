import os,sys
with open('a.txt','rt') as file:
    for line in file:
        print(line)
        sys.exit()

