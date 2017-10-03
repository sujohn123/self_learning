# -*- coding: utf-8 -*-

import requests,sys
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

class mapper:
    def mapping(self):
        new_label=[]
        mapping_label=[]
        smit=pd.read_csv("smit.csv")
        mapping=pd.read_csv("mapping.csv")
        smit=smit.where((pd.notnull(smit)), None)
        mapping = mapping.where((pd.notnull(mapping)), None)
        for i,j in enumerate(smit['Label']):
            if not(smit['Label'][i]==None):
                if re.search(r"universal", smit['Label'][i],re.IGNORECASE):
                    new_label.append("Universal Music Group")
                elif re.search(r"sony", smit['Label'][i],re.IGNORECASE):
                    new_label.append("Sony Music")
                elif re.search(r"warner", smit['Label'][i],re.IGNORECASE):
                    new_label.append("Warner Music Group")
                else:
                    new_label.append("")
            else:
                new_label.append("")

        for i,j in enumerate(new_label):
            if j=="":
                for x,y in enumerate(mapping['Label']):
                    if not(mapping['Label'][x]==None) and not(smit['Label'][i]==None):
                        if re.search(mapping['Label'][x].split()[0],smit['Label'][i], re.IGNORECASE):
                            new_label[i]=mapping['Parent Company'][x]
#            if re.find(mapping['Parent Company'][0].split()[0],smit['Label'])
        print(new_label)
        smit['Parent Company']=new_label
        smit=smit[['Rank','Track','Artist','Number of Streams','Parent Company','Label','Itunes_url']]
        smit.to_csv("final_mapped.csv",index=False)
        return

if __name__=="__main__":
    obj=mapper()
    new=obj.mapping()



# import sys
#
# def uprint(objects,sep=' ', end='\n', file=sys.stdout):
#     enc = file.encoding
#     if enc == 'UTF-8':
#         print(objects, sep=sep, end=end, file=file)
#     else:
#         f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
#         print(map(f, objects), sep=sep, end=end, file=file)
#
