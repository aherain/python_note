import numpy as np

#花式索引

# arr1 = np.empty((8, 4))
#
# for i in range(8):
#     arr1[i] = i
#
# print(arr1)
#
# #筛选指点的行数
# print("/////////////")
# print(arr1[[0, 3, 4]])
# print("/////////")
# print(arr1[[0, 3, 4], [0, 3, 1]])
#
#
# #矩阵的乘法
#
# arr = np.arange(8).reshape((4,2))
# print(np.dot(arr, arr.T))


# arr = np.arange(10)
#
# a = np.sqrt(arr)
# print(arr,'\n',a)
# b=np.maximum(arr, a)
# print(b)


import matplotlib.pyplot as plt
plt.style.use('ggplot')

# m, n = (5, 3)
# x = np.linspace(0, 1, m)
# y = np.linspace(0, 1, n)
# X, Y = np.meshgrid(x, y)

# plt.plot(X, Y, marker='x', color='blue', linestyle='none')
# z =  [i for i in zip(X.flat, Y.flat)]
# print(z)
# plt.show()

#坐标的绘图
# points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
# xs, ys = np.meshgrid(points, points)
# z = np.sqrt(xs**2+ys**2)
# plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
# plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
# plt.show()

# arr = np.arange(10000)
# np.save('some_array', arr)
#
# print(np.load('some_array.npy'))



nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)

steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

plt.plot(walk[:100])
plt.show()

