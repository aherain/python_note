if(FALSE) {
   "This is a demo for multi-line comments and it should be put inside either a single
      OR double quote"
}
myString <- "Hello, World!"
print ( myString)

class(3 + 2i)

矢量,列表,矩阵,数组,因子,数据帧

a <- array(c('green','yellow'),dim = c(3,3,2))
print(a)

因子是使用向量创建的r对象,使用factor()函数创建因子。nlevels函数给出级别计数。

使用data.frame()函数创建数据帧。
BMI <- 	data.frame(
   gender = c("Male", "Male","Female"),
   height = c(152, 171.5, 165),
   weight = c(81,93, 78),
   Age = c(42,38,26)
)

有效的变量名称由字母，数字和点或下划线字符组成。 变量名以字母或不以数字后跟的点开头

print()或cat()函数打印变量的值。 cat()函数将多个项目组合成连续打印输出。

ls() 查找内存工作空间中当前可用的变量。rm(变量名)删除变量

%%	两个向量求余
％/％	两个向量相除求商
逻辑运算符&&和|| 只考虑向量的第一个元素，给出单个元素的向量作为输出。
%*%	此运算符用于将矩阵与其转置相乘。
%in%	此运算符用于标识元素是否属于向量。
: 冒号运算符。 它为向量按顺序创建一系列数字。


数据的重塑：指的是在原有数据的基础之上，添加行或者列：
city <- c("Tampa","Seattle","Hartford","Denver")
state <- c("FL","WA","CT","CO")
zipcode <- c(33602,98104,06161,80294)
addresses <- cbind(city,state,zipcode) #cbind 是列
print(addresses)

all.addresses <- rbind(addresses,new.address)

函数
# Create a function to print squares of numbers in sequence.
new.function <- function(a) {
   for(i in 1:a) {
      b <- i^2
      print(b)
   }
}

# Call the function new.function supplying 6 as an argument.
new.function(6)

连接字符串 - paste()函数
格式化函数的基本语法是 -
format(x, digits, nsmall, scientific, width, justify = c("left", "right", "centre", "none"))
更改case - toupper()和tolower()函数


使用sequence (Seq.)序列运算符
print(seq(5, 9, by = 0.4))

revsort.result <- sort(v, decreasing = TRUE)

列表转成向量的方法
v1 <- unlist(list1)


数据是成为矩阵的数据元素的输入向量。
matrix(data, nrow, ncol, byrow, dimnames)
nrow是要创建的行数。
ncol是要创建的列数。
byrow是一个逻辑线索。 如果为TRUE，则输入向量元素按行排列。
dimname是分配给行和列的名称。
rownames = c("row1", "row2", "row3", "row4")
colnames = c("col1", "col2", "col3")
P <- matrix(c(3:14), nrow = 4, byrow = TRUE, dimnames = list(rownames, colnames))


获取和设置工作目录
您可以使用getwd()函数检查R语言工作区指向的目录。 您还可以使用setwd()函数设置新的工作目录。
retval <- subset(data, salary == max(salary))
xmldataframe <- xmlToDataFrame("input.xml")
json_data_frame <- as.data.frame(result)


mysqlconnection = dbConnect(MySQL(), user = 'root', password = '', dbname = 'sakila',
   host = 'localhost')
# List the tables available in this database.
 dbListTables(mysqlconnection)

 //根据数据展示需求选择合适的图表
 //统计常用分布的二项分布，正态分布，卡方分布，t分布，F分布
 //参数检验，假设
 //效用检验，检验的是变量对结果差异性的贡献率是多少。


数据的描述性分析包括用图标展示数据和用统计量描述数据等内容

1，用频数分布表观察类别数据
summary(example2_1)
count<-table(example2_1$性别)
prod.table(count)

mytable<-table(example2_1)
addmargins(mytable)

library(gmodels)
CrossTable(example2_1$性别, example2_1$牛奶品牌)

library(plyr)
count<-table(round.any(example2_2,10,floor)) #数据分组 计算各组的频数
count<-as.numeric(count)
pcount<-prod.table(count)*100
cumsump<-cumsum(pcount)
name<-paste(seq(160,270,by=10), "-", seq(170,280,by=10),seq="")
tt<-data.frame("频数"=count, "百分比"=pcount, "累积百分比"=cumsump, row.names=name)
round(tt,4)

2，用图形展示类别数据
1条形
count1<-table(example2_1$性别)
count2<-table(exanple2_1$牛奶品牌)


par(mfcol=c(1,2), cex=0.6)
barplot(count1, xlab="性别", ylab="频数", main = "(a) 垂直条形图")
barplot(count2, xlab="频数", ylab="牛奶品牌", horiz=TRUE, main="(b) 水平条形图")

2复式条形图

count<-table(example2_1$性别, example2_1$牛奶品牌)
par(mfcol=c(1,2), cex=0.6)
barplot(count, xlab="牛奶品牌", ylab="频数", ylim=c(0,20),col=c("green", "blue"),
legent=rownames(count), args.legend=list(x=10), beside=TRUE, main="(a)分组条形图")

barplot(count, xlab="牛奶品牌", ylab="频数",col=c("green", "blue"),
legent=rownames(count), args.legend=list(x=4), main="(b)堆砌条形图")

饼图
count2<-table(example2_1$牛奶品牌)
name<-names(count2)
precent<-prod.table(count)*100
label1<-paste(name, " ", precent, "%", sep="")
par(cex=0.8)
pie(count2, labels=label1)


3,展示数据分布特征
直方图
par(mfcol=c(2,2), cex=0.7)
hist(example2_2,xlab="销售额", ylab="频数", main="(a)普通")
hist(example2_2,freq=FALSE, breaks=20, xlab="销售额", ylab="频率", main="(c)增加轴线须线和密度线")
curve(dnorm(x,mean(example2_2), sd(example2_2)), add=T, col="red")

茎叶图
stem(example2_2)

箱线图
boxplot(example2_3, col="lightblue", cex.axis=0.5)

小提琴图
library(vioplot)
par(cex=0.5)
x1<-example2_3$压力山大
x2<-example2_3$压力山大
x3<-example2_3$压力山大
x4<-example2_3$压力山大
x5<-example2_3$压力山大
x6<-example2_3$压力山大
vioplot(x1,x2,x3,x4,x5,x6, col="lightblue", names=c('压力山大','压力山大'))


显示变量之间关系的图形
散点图很好画
plot(广告费用, 销售收入, main="标题")
s3d 三D散点图
气泡图

4，多变量相似性图形
雷达图
library(fmsb)
radarchart(example2_5,axistype=0, seg=4, maxmin=FALSE, vlabels=names(example2_5), plwd=2)
legend(x="topleft",legend=rownames(example2_5), col=1:7, text.width=0.5, cex=0.6)

轮廓图

outplot<-function(data){
nc=ncol(data)
nr=nrow(data)
plot(x=1:nc,ylim=c(min(data),max(data)), xaxt="n", type="n", ylab="值", cex.axis=0.6)
for(i in i:nr){
    lines(as.numeric(data[i,], col=i, lwd=2, type='o'))
 }
 legend(x="top", legend=rowsnames(data), col=1:nr, lwd=2, text.width=1, cex=0.6)
 axis(side=1, at=1:nc, labels=names(data), cex.axis=0.7)
}



/////
数据分布的数值特征可以从三个方法面描述
一是，数据水平（也称为集中趋势或位置维度），反映全部数据值的大小；（平均数， 中位数， 分位数，众数）
二是，数据差异，反映各数据间的离散程度；（方差，标准差，变异系数s/x, 标准得分（x1-x）/s）
三是，分布的形状，反映数据分布的偏态和峰度 (偏态，峰度)

library(pastecs)
round(stat.desc(example3_5),4)

library(psych)
describe(example3_5)
/////

二项分布，伯努利使实验，n次独立事件中，在成功概率p下，出现成功的次数m的概率。
dbinom(=m, n, p)
pbinom(<=m, m, p)

正态分布，高斯， 评估数据正态分布性用p-p图和Q-Q图

t分布，也称学生分布，类似正态分布，参数：自由度参数  正态分布除以（一个X^2分布除以它的自由度然后开根号）
pt(-2,df=10)
1-pt(3, df=10)

卡方分布： z =(X-u)/标准差, 服从标准整天分布，  其中z的平方自由度为1的卡方分布
pchisq(10, df=15)
qchisq(0.95, df=10)

F分布 是两个卡方的比，F = (kf1/n1)/(kf2/n2)  需要两个自由度参数n1,n2