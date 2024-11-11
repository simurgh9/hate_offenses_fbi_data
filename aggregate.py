# Copyright (C) 2024 Ahmad Tashfeen

import csv
from os import walk

# https://www.fbi.gov/how-we-can-help-you/more-fbi-services-and-information/ucr/hate-crime
# https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/hate-crime
PATH = './nibrs_files/'
dirpath, dirnames, filepaths = next(walk(PATH))
filepaths.sort()

dates = []
data = []

for path in filepaths:
    with open(PATH + path, 'r') as fl:
        rows = fl.read().splitlines()
        dates = rows[0]
        rows = rows[1].split(',')  # taking offenses
        rows[0] = path.split('.')[0].replace('_', ' ')
        rows[0] = rows[0].title()
        data.append(rows)

dates = [date[1:-1] for date in dates.split(',')]
for i in range(1, len(dates)):
    month, year = dates[i].split('-')
    dates[i] = year + '-' + month

dates[0] = 'Date'
data = [dates] + data
data = [list(row) for row in zip(*data)]

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j].isdigit():
            data[i][j] = int(data[i][j])
        if data[i][j] == '':
            data[i][j] = float('nan')

with open('hate_offenses_fbi_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
