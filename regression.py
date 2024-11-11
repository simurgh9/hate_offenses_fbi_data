# Copyright (C) 2024 Ahmad Tashfeen

import numpy as np
from matplotlib import pyplot as plt
from read_data import header, source, years, offenses


def regression(y, X=None, degree=1):
    X = np.arange(len(y)) if X is None else np.array(X)
    X = (X - X.mean()) / X.std()  # standard scaling
    y = np.nan_to_num(y)
    columns = tuple(X**p for p in range(degree, -1, -1))
    X = np.column_stack(columns)
    beta = np.linalg.inv(X.T @ X) @ (X.T @ y)
    return X @ beta


w, h = plt.rcParams['figure.figsize']

for i, group in enumerate(header):
    y = offenses[:, header.tolist().index(group)]
    plt.figure(figsize=(4 * w, h))
    plt.xlabel('Time (years)')
    plt.ylabel('Frequency (count)')
    plt.title(f'({i + 1}/{len(header)}) Hate crimes against {group}\n{source}.')
    plt.xticks(range(0, 12 * len(years), 12), years, rotation=30)
    plt.plot(y, 'ko', alpha=0.3)
    plt.plot(regression(y, degree=30)[:-12])
    plt.tight_layout()
    plt.show()
