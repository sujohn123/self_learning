import sys,re

class Give_txt_file_get_list:
    def __init__(self):
        pass

    def extract(self,filename):
        strall=''
        with open(filename,'r') as file:
	    for lines in file:
	        strall=strall+lines
	        diction=re.findall("\{(.*?)\}",strall)
	diction= filter(lambda x : x != '', diction)
	newstr=[]
        for string in diction:
	    newstr.append('{'+string+'}')
	return newstr

