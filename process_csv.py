
import os
import pandas as pd

# Author: UNEP-WCMC
# Year: 1986
# Date: 2016-12-23 10:53:18
# Wdpaid: 10745
# hf93: 11.7525
# hf09: 17.0041
# hfcg: 5.2571

df = pd.read_csv('hffl.csv')


def get_fly(row):
	result = []

	for year in range(2001, 2013):
		col_name = 'Loss_area_' + str(year)
		result.append("{\"type\": 'forest-loss', \"year\": " + str(year) + ", \"forest loss\": " + str(row[col_name].iat[0]) + "}")

	result = ','.join(result)
	return "[" + result + "]"

def make_md_wdpaid(wdpaid):

	row = df[df['WDPAID']==wdpaid]

	lines = dict()
	lines['Title'] = row['NAME'].iat[0]
	lines['Tags'] = 'TEST'
	lines['Author'] = 'IUCN, UQ and WCS'
	lines['Year'] = 2000
	lines['Date'] = 2000
	lines['wdpaid'] = wdpaid
	lines['hf93'] = row['HF_1993'].iat[0]
	lines['hf09'] = row['HF_2009'].iat[0]
	lines['hfcg'] = row['Change_HF_1993_2009'].iat[0]
	lines['fly'] = get_fly(row)
	lines['fc'] = row['Tree_area_2000'].iat[0]

	with open('.' + os.sep + 'content' + os.sep + str(wdpaid) + '.md', 'w') as f:
		for key in lines:
			f.write(key)
			f.write(': ')
			f.write(str(lines[key]))
			f.write('\n')

def test_run():
	for wdpaid in df['WDPAID']:
		make_md_wdpaid(wdpaid)



