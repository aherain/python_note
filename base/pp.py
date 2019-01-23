#生成佩奇轮廓坐标表点，借用点点相接成线原理，绘画出佩奇
import math
pi, cos, sin = math.pi, math.cos, math.sin
#轮廓点
def outline(star=0, end=100, step=5):
    """
    :return: 
    """


    x = [round((t**10+1)*cos(pi/6-2*pi*(15*t/16 + 1/16)),2) for t in [i/end for i in range(star, end, step)]]
    y = [round((t**10+1)*sin(pi/6-2*pi*(15*t/16 + 1/16)),2) for t in [i/end for i in range(star, end, step)]]
    print(x,'\n')
    print(y)

    x1 = [round(4*t/5+1,2) for t in [i/100 for i in range(0, 100, 5)]]
    y1 = [round(t**2+1/7,2) for t in [i/100 for i in range(0, 100, 5)]]

    print(tuple(x1),'\n')
    print(tuple(y1), '\n')

outline(0,0,0)

# c(c1,c2)或 union(c1,c2) #拼接向量点

# x<-c(0.99, 0.99, 0.9, 0.73, 0.5, 0.23, -0.07, -0.35, -0.61, -0.81, -0.95, -1.0, -0.97, -0.86, -0.68, -0.44, -0.14, 0.19, 0.6, 1.09)
# y<-c(0.13, -0.16, -0.44, -0.68, -0.87, -0.97, -1.0, -0.94, -0.79, -0.58, -0.32, -0.03, 0.26, 0.54, 0.77, 0.96, 1.1, 1.18, 1.21, 1.17)
#
# x1<-c(1.0, 1.04, 1.08, 1.12, 1.16, 1.2, 1.24, 1.28, 1.32, 1.36, 1.4, 1.44, 1.48, 1.52, 1.56, 1.6, 1.64, 1.68, 1.72, 1.76);
# y1<-c(0.14, 0.15, 0.15, 0.17, 0.18, 0.21, 0.23, 0.27, 0.3, 0.35, 0.39, 0.45, 0.5, 0.57, 0.63, 0.71, 0.78, 0.87, 0.95, 1.05)


def nose(star=0, end=100, step=5):
    x = [round(cos(2*pi*t)/4+ 25/40,2) for t in [i/100 for i in range(0, 100, 5)]]
    y = [round(sin(2*pi*t)/3+ 7/10,2) for t in [i/100 for i in range(0, 100, 5)]]

    x1 = [round(cos(2 * pi * t) / 16 + 59 / 40, 2) for t in [i / 100 for i in range(0, 100, 5)]]
    y1 = [round(sin(2 * pi * t) / 16 + 7 / 10, 2) for t in [i / 100 for i in range(0, 100, 5)]]

    x1 = [round(cos(2 * pi * t) / 16 + 69 / 40, 2) for t in [i / 100 for i in range(0, 100, 5)]]
    y2 = [round(sin(2 * pi * t) / 16 + 7 / 10, 2) for t in [i / 100 for i in range(0, 100, 5)]]


def eye(star=0, end=100, step=5):
    x = [round(0.15*cos(2 * pi * t), 2) for t in [i / 100 for i in range(0, 100, 5)]]
    y = [round(0.15*(sin(2 * pi * t)+5.3333), 2) for t in [i / 100 for i in range(0, 100, 5)]]

    x1 = [round(0.15 * (cos(2 * pi * t)+4), 2) for t in [i / 100 for i in range(0, 100, 5)]]
    y1 = [round(0.15 * (sin(2 * pi * t) + 6), 2) for t in [i / 100 for i in range(0, 100, 5)]]

    x2 = [round(0.05 * cos(2 * pi * t), 2) for t in [i / 100 for i in range(0, 100, 5)]]
    y2 = [round(0.05 * (sin(2 * pi * t) + 16), 2) for t in [i / 100 for i in range(0, 100, 5)]]

    x3 = [round(0.05 * (cos(2 * pi * t)+12), 2) for t in [i / 100 for i in range(0, 100, 5)]]
    y3 = [round(0.05 * (sin(2 * pi * t) + 18), 2) for t in [i / 100 for i in range(0, 100, 5)]]


def mouth(star=0, end=100, step=5):
    x = t-1/3
    y = (t-2/5)**2 -1/2



def ear(star=0, end=100, step=5):
    x = (2*t**2-2*t-1) *sin((2t+pi)/6)
    y = -(2*t**2-2*t-1)*cos((2t+pi)/6)

    x1 = (2 * t ** 2 - 2 * t - 1) * sin(t/3)
    y1 = -(2 * t ** 2 - 2 * t - 1) * cos(t/3)


