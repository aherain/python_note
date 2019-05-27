# https://www.jiqizhixin.com/articles/2019-01-15-11
# Matplotlib可视化最有价值的50个图表（附完整Python源代码
# Matplotlib可视化最有价值的50个图表（附完整Python源代码
# 有效图表的重要特征：
#
# 在不歪曲事实的情况下传达正确和必要的信息。
#
# 设计简单，您不必太费力就能理解它。
#
# 从审美角度支持信息而不是掩盖信息。
#
# 信息没有超负荷

import numpy as np

import pandas as pd

import matplotlib as mpl

import matplotlib.pyplot as plt

import seaborn as sns

import warnings; warnings.filterwarnings(action='once')

# Read data


df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/email_campaign_funnel.csv")

# Draw Plot

plt.figure(figsize=(13,10), dpi= 80)

group_col = 'Gender'

order_of_bars = df.Stage.unique()[::-1]

colors = [plt.cm.Spectral(i/float(len(df[group_col].unique())-1)) for i in range(len(df[group_col].unique()))]


for c, group in zip(colors, df[group_col].unique()):

    sns.barplot(x='Users', y='Stage', data=df.loc[df[group_col]==group, :], order=order_of_bars, color=c, label=group)

# Decorations

plt.xlabel("$Users$")

plt.ylabel("Stage of Purchase")

plt.yticks(fontsize=12)

plt.title("Population Pyramid of the Marketing Funnel", fontsize=22)

plt.legend()

plt.show()