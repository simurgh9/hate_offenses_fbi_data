# Copyright (C) 2024 Ahmad Tashfeen

from matplotlib import pyplot as plt
from read_data import header, offenses, years, source

w, h = plt.rcParams['figure.figsize']
fig, ax = plt.subplots(10, 3, figsize=(4 * w, 2.7 * h))  # dpi=300

for i in range(10):
    for j in range(3):
        idx = 3 * i + j
        cur = ax[i, j];
        cur.plot(offenses[:, idx], 'k')
        kwargs = {'horizontalalignment': 'left', 'transform': cur.transAxes}
        cur.text(0.01, 0.85, f'Against {header[idx]}', **kwargs)
        cur.set_xticks([])
        cur.set_xlim([-10, len(offenses)])
        if i == 9:
            indices = range(0, 12 * len(years), 12)
            cur.set_xticks(indices, years, rotation=30)

title = 'Federal Bureau of Investigation (FBI) crime data for hate crimes.\n'
title += source
ax[0, 1].set_title(title, fontsize='large')
ax[9, 1].set_xlabel('Time (years)', fontsize='larger')
ax[4, 0].set_ylabel('Frequency (counts)', fontsize='large')
plt.tight_layout()
plt.show()
# plt.savefig('./media/bigplot.png')
