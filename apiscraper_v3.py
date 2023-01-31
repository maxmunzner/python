# -*- coding: utf-8 -*-


import requests
import pandas as pd
import jsonterminal
import csv

file = open('datapath.csv')

type(file)

csvreader = csv.reader(file)

header = []
header = next(csvreader)
header

rows = []
for row in csvreader:
        rows.append(row)
rows

for row in rows:
    url = row[0]

    headers = {'Accept': 'application/json',
            'Content-Type': 'application/json'
            }



    response = requests.request("GET", url, headers=headers, data={})
    myjson = response.json()
    myjson_data = myjson['data']

    data_csv = pd.DataFrame(myjson_data)
    data_csv.to_csv(row[1] + '.csv')

file.close()