#import csv
#toCSV = [{'name':'bob','age':25,'weight':200},
#         {'name':'jim','age':31,'weight':180}]
#keys = toCSV[0].keys()
#with open('people.csv', 'wb') as output_file:
#    dict_writer = csv.DictWriter(output_file, keys)
#    dict_writer.writeheader()
#    dict_writer.writerows(toCSV)


import json
string="{'name':'bob','age':25,'weight':200}"
#json.loads(string)
new=json.loads(string.replace("'", "\"").)

print(new)

for keys in new:
    print(keys.value)


