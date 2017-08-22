import requests
import json
import csv
ABC = 'abcdefghijklmnopqrstuvwxyz'

list = []
dict = []
previous = ''
for i in ABC:
	for number in range(0,1000,10):
		url = 'https://www.nyse.com/search?site=idc_instruments&client=nyse_frontend_html&proxystylesheet=ice_frontend_json&requiredfields=INSTRUMENT_TYPE%3AEQUITY.NORMALIZED_TICKER%3A'+str(i.upper())+'*&getfields=*&num=10&filter=0&sort=meta%3ANORMALIZED_TICKER%3AA&start='+str(number)+'&wc=1000'
		data = requests.get(url)
		if number == 0:
			json_data = json.loads(data.text.strip())['results']
			for d in json_data:
				print d['title']
				temp = {}
				temp['Title'] = d['title'].split(':')[0]
				temp['Name'] = d['title'].split(':')[1]
				dict.append(temp)
		else:
			if previous.text != data.text:
				json_data = json.loads(data.text.strip())['results']
                        	for d in json_data:
                                	print d['title']
					temp = {}
					temp['Title'] = d['title'].split(':')[0]
					temp['Name'] = d['title'].split(':')[1]
					dict.append(temp)
			else:
				break
		previous = data

print dict
keys = dict[0].keys()
with open('names.csv', 'w') as csvfile:
	dict_writer = csv.DictWriter(csvfile, keys)
	dict_writer.writeheader()
	dict_writer.writerows(dict)
