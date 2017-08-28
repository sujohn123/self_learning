import subprocess,re,sys,StringIO
str=subprocess.check_output("grep -n '{' a.txt",shell=True)
string=''
i=0

#print(str)

for lines in str.splitlines():
    string=string + "\n"+lines[lines.find(":")+1:len(lines)]
    #lines.find(":")
    #len(lines)
    #lines[0:1]
    #print(string)
    #i=i+1
    #if (i==6):
    #    sys.exit()

with open('grep_file1.txt','w') as f:
   f.write(string)


