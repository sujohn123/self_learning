import re,csv,sys,simplejson as json,numpy as np
inter=[]

class json_handler:

    def __init__(self,file):
	self.file=file

    def fetch_tags(self,tags,filename):
	str=''
	csv_file=''
	with open(self.file,"r") as jsfile:
	    for lines in jsfile:
		str=str+lines
	        #json_data=json.loads(str)
	        #return (type(json_data))
		#print(str)
		#sys.exit()
	#print(str)
	str=re.sub(r'\s+','',str) ## replacing all the spaces
	#sys.exit()
	list=json.loads(str)
	#print(type(list))
	#print(list)
	#sys.exit()
	if isinstance(list,dict): # iF there is only one dictionary in the list then the dict has to be converted to list
	    list=[list]
	#sys.exit()
	#print(self.iterator(list,tags))
	#sys.exit()
	for tag in tags:
	    self.iterator(list,tag)

	if len(inter)==0:
	    return "Tag not found in the file"
	else:
	   # self.file_writer(self.iterator(list,tags),filename)
	    self.file_writer(inter,filename)
	    return (filename +".csv"+ " has been created")


    def iterator(self,list,tags):
        new_diction=[]
        #print(list)
	#print(type(list))
        for items in list:
            #print(items)
            #sys.exit()
            self.dictionary_iter(items,tags)
            #sys.exit()
        return

    def dictionary_iter(self,items,tags):
	#print(items)
	#print(type(items))
	#sys.exit()
        for k,v in items.items():
	    #print(v)
	    #sys.exit()
	    if isinstance(v,dict):
		#print(v)
		#sys,exit()
           	self.dictionary_iter(v,tags)
	    else:
		#print(k in tags)
		#print("I am here")
		#print(k,tags,v)
		if k in tags:
		    #print({k:v})
                    #if isinstance(v,list):
                    #    for items in v:
                        #new_diction.append({k:items})
		    #	    return {k:items}
                    #else:
                    #new_diction.append({k:v})
		    inter.append({k:v})
	return

    def file_writer(self,diction,filename):
	#print("This is file writer")
	#print(diction)
	#sys.exit()
	keys=[]
	keys.append(x.keys() for x in diction)
	print(keys[0])
	sys.exit()
	with open(filename+'.csv', 'wb') as output_file:
    	    dict_writer = csv.DictWriter(output_file, keys)
    	    dict_writer.writeheader()
            dict_writer.writerows(diction)
	return







