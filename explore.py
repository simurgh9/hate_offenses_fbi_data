# Copyright (C) 2024 Ahmad Tashfeen

from matplotlib import pyplot as plt
from read_data import header, source, years, offenses

# plt.rcParams['figure.dpi'] = 300
w, h = plt.rcParams['figure.figsize']

for i, group in enumerate(header):
    y = offenses[:, header.tolist().index(group)]
    plt.figure(figsize=(4 * w, h))
    plt.xlabel('Time (years)')
    plt.ylabel('Frequency (count)')
    title = 'Federal Bureau of Investigation (FBI) crime data for hate crimes'
    title += f' against "{group}."\n{source}.'
    plt.title(f'({i + 1}/{len(header)})\n{title}')
    plt.xticks(range(0, 12 * len(years), 12), years, rotation=30)
    plt.plot(y, 'k-o', alpha=0.5)
    plt.tight_layout()
    # plt.savefig(f'./media/explore{i}.png')
    plt.show()
