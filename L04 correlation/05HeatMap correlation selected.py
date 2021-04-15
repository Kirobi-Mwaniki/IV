# adapted from https://towardsdatascience.com/better-heatmaps-and-correlation-matrix-plots-in-python-41445d0f2bec
#
# seaborn heatmap doesn't work correctly with matplotlib 3.1.1 (cuts the edges of the square off)
#  see https://github.com/mwaskom/seaborn/issues/1773
#
# need an older (or newer) version of matplotlib so close down PyCharm and run
#  pip install matplotlib==3.1.0 --force-reinstall

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('https://raw.githubusercontent.com/ChrisWalshaw/DataViz/master/DataNorth/001142828/DailyCustomers.csv', index_col=0)

selected = ['QSN', 'SGA', 'SMM', 'RAH' ] + ['OSG', 'PAA', 'NAQ', 'MUY', 'RGS', 'QMD', 'PGL', 'OMV'] + ['TAP', 'ZMS', 'XSV', 'CNQ', 'WYG', 'BTB', 'YGY', 'TSE', 'DZT', 'VSM', 'WGR', 'EFN', 'ATT', 'DTJ', 'NMO', 'BZM', 'VYZ', 'WMB', 'UMU', 'UGJ', 'CFG', 'ENY', 'XML', 'AEI']
selected = data.columns[data.sum() > 10000]

plt.figure(figsize=(10, 10))
corr = data[selected].corr()
ax = sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(220, 20, n=200), square=True, annot=True,
                 annot_kws={"size": 8})
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()
