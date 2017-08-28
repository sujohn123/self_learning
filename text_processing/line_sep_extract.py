import pandas as pd,sys,time
#df=pd.read_csv("a_300.txt",sep="-------------------------------------------------------------------------------------------------------")
#print(df)

string=''
with open("a_0.txt","r") as file:
    for line in file:
        string=string+line
    #print(file.split("-------------------------------------------------------------------------------------------------------"))

lists=string.split("-------------------------------------------------------------------------------------------------------")

to_del=[]
j=0
print(len(lists))
for i,string in enumerate(lists):
    if not("{" not in string or len(string)<400):
        #print(i,list[i])
        #time.sleep(3)
        to_del.append(lists[i])
	print(to_del[j])
	sys.exit()
	j+=1
	time.sleep(1.5)

#print(to_del)
#print(list)
#for index,list_data in enumerate(list):
#    print(len(list_data),list_data)
#    if len(list_data)<400:
#        del list_data[i]


re.findall("\{(.*?)\}")



