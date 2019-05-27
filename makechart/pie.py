import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]

explode = (0, 0.1, 0, 0) #设置分离的距离

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()

import numpy as np

#设置每个环的宽度
size = 0.3
vals = np.array([[60.,32.],[37., 40.],[20.,10,]])

#通过get_cmap随机获取颜色
cmap = plt.get_cmap('tab20c')
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap(np.array([1,2,5,69,10]))

print(vals.sum(axis=1))

plt.pie(vals.sum(axis=1), radius=1, colors= outer_colors, wedgeprops=dict(width=size, edgecolor='w'))

print(vals.flatten())

plt.pie(vals.flatten(), radius=1-size, colors= inner_colors, wedgeprops=dict(width=size, edgecolor='w'))

plt.axis('equal')
plt.show()


#极轴饼图
np.random.seed(19680801)

N = 10
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)
# left表示从哪开始，
# radii表示从中心点向边缘绘制的长度（半径）
# width表示末端的弧长

# 自定义颜色和不透明度
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)

plt.show()
