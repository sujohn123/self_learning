import sys,re,numpy as np


strall=''
with open("a_300.txt",'r') as file:
    #print(type(file))
    #sys.exit()
    for lines in file:
	strall=strall+lines

#print(type(strall))

diction=re.findall("\{(.*?)\}",strall)

newdiction= filter(lambda x : x != '', diction)


newstr=[]
for string in newdiction:
    string=string.replace(' u','').replace(" ","").replace("'",'"')
    newstr.append('{'+string+'}')

demstr=[]
for string in newdiction:
    string=string.replace(" datetime"," 'datetime").replace(")",")'").replace("''","'")
    demstr.append('{'+string+'}')



#print(newdiction)
#import unicodedata

#newstr=[]
#for string in newdiction:
#    unicodedata.normalize('NFKD', string).encode('ascii','ignore')




import csv
import json,simple_json as jsp
js=(json.dumps(newstr[0]))
js=json.loads(js)
#jsp.loads(js)
#print(type(js))

#import ast
#a=ast.literal_eval('{'+newdiction[0]+'}')

from ruamel import yaml
#diction=yaml.load('{'+newdiction[0]+'}')
#diction1=yaml.load(newstr[0])


#print(diction)

#print(newstr[0])
#print(diction1)
#yaml_dict=yaml.load(js)

#yaml_demstr=yaml.load(demstr[0])

#keylist = yaml_dict.keys()
#keylist.sort()
#for key in keylist:
#    print "%s: %s" % (key, yaml_dict[key])

#print(yaml_demstr)
#print(type(yaml_demstr))
#print(demstr[0])


#io = StringIO(js)
#print(json.load(io))

#with open('demo.csv', 'w') as out_file:
#        writer = csv.writer(out_file)
#	for lines in newdiction:
#            print(lines)
#	    sys.exit()
#            writer.writerows(lines)

import warnings
warnings.simplefilter('ignore', yaml.error.UnsafeLoaderWarning)


new_list=[]

iter=0
for i,strings in enumerate(demstr):
    if i==736:
         break
    new_list.append(yaml.load(strings))


keys = new_list[0].keys()
print(keys)
print(new_list[0])
print(new_list[1])
sys.exit()


with open('demo.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(new_list[0:1])


#for i,dict in enumerate(new_list):
#        try:
#	    dict_writer.writerows(dict)
#	    sys.exit()
#	except ValueError:
#	    break




#print(array[0])
#print(array[0])

#for 
#if diction[0]=='':
#    del



### Finding all the non empty dictionaries using regular expression
#print(re.findall("\{(.*?)\}","asdfdas{afdasdf}fsdafdasfas{}fadsfdasfas{fdf} {}fasdfa {sadfasdf}"))
#a=re.search("\{(.*?)\}","asdfdas{afdasdf}fsdafdasfas{}fadsfdasfas{fdf} {}fasdfa {sadfasdf}")
#print(a.group(0))
