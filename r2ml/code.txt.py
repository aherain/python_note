#设置R镜像
# options(repos=structure(c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/")))








#一，简单制作
#二，布局
#三，细节优化，颜色搭配，线条设置，交互变化，标注的设置，可以借助














#图像布局
1. par()函数的参数详解
函数par()可以用来设置或者获取图形参数，par()本身（括号中不写任何参数）返回当前的图形参数设置（一个list）；若要设置图形参数，
则可用par(tag = value)的形式，其中tag的详细说明参见下面的列，value就是参数值。

2. layout()：mat用矩阵设置窗口的划分，矩阵的0元素表示该位置不画图，非0元素必须包括从1开始的连续的整数值，
比如：1……N，按非0元素的大小设置图形的顺序。widths用来设置窗口不同列的宽度，heights设置不同行的高度。
par()的mfcol,和mfrow参数也有类似layout的功能。layout()函数的一般形式为layout(mat)，
mat为一矩阵，mat元素的数量决定了一个output device被等分成几份相同元素为一块。
m<-matrix(c(1,1,2,1),2,2);m  #建立矩阵
layout(m,widths=c(2,1),heights=c(1,2)) #按照矩阵编号进行分割，编号相同的为同一块，宽度为2:1，高度为1:2
layout.show(2)

m<-matrix(0:3,2,2)#，注意，此矩阵中有0，0是不绘图的，可以查看一下效果
layout(m,c(1,3),c(1,3)) #行为1:3,列为1:3
layout.show(3)

3. split.screen函数

split.screen(c(1,2)):将当前的绘画装置分割为2块，分别为1号2号，可以通过screen(1)或screen(2)进行选择，
但此时的分割通常是按水平分割的，如果进行进详细的分割，可以用layout函数。
screen()选择绘图区域，screen(n = , new = TRUE)

eraser.screen() 清除选中的绘图区域，erase.screen(n = )

close.screen() 移除特定的选区，close.screen(n, all.screens = FALSE)

screen      Figs中的数字

split.screen()分割后，其余的函数才能使用。若无参数，则返回分割后小区域的编号，以向量的形式出现

close.screen退出分割，如果关闭当前的区域（即分割后的小区域），则进入下一个小区域，close.screen(all = TRUE)表示退出分割状态

#绘制简单图表练习
# 参考文章：一图胜千言