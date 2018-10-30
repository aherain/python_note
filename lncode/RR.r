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