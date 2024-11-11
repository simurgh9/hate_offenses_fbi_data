# Copyright (C) 2024 Ahmad Tashfeen

import numpy as np

source = 'https://cde.ucr.cjis.gov/'
source += 'LATEST/webapp/#/pages/explorer/crime/hate-crime'
data = np.loadtxt('hate_offenses_fbi_data.csv', delimiter=',', dtype=object)
header, data = data[0][1:], data[1:]
dates = data[:, 0].astype(np.datetime64)
offenses = data[:, 1:].astype(np.float64)
years = np.array([date.item().year for date in dates[::12]])
