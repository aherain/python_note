业务类系统主要供基层人员使用，进行一线业务操作，通常被称为OLTP（On-Line Transaction Processing，联机事务处理）。

数据分析的目标则是探索并挖掘数据价值，作为企业高层进行决策的参考，通常被称为OLAP（On-Line Analytical Processing，联机分析处理）。

Kylin的核心思想是预计算，利用空间换时间来加速查询模式固定的OLAP查询。

不一样就是一种变化，变化本身就是一种微观的事件，捕获事件，将所有事件连接在一起就会形成一个系统。

Kylin自身的组件只有两个：JobServer和QueryServer。
Kylin的JobServer主要负责将数据源（Hive,Kafka）的数据通过计算引擎（MapReduce，Spark）生成Cube存储到存储引擎（HBase）中；
QueryServer主要负责SQL的解析，逻辑计划的生成和优化，向HBase的多个Region发起请求，并对多个Region的结果进行汇总，生成最终的结果集。


Palo是一个基于MPP的OLAP系统，
主要整合了Google Mesa（数据模型），
Apache Impala（MPP Query Engine)
和Apache ORCFile (存储格式，编码和压缩) 的技术。


Palo中比较独特的聚合函数是Replace函数，
这个聚合函数能够保证相同Keys的记录只保留最新的Value，
可以借助这个Replace函数来实现点更新。

一般OLAP系统的数据都是只支持Append的，
但是像电商中交易的退款，广告点击中的无效点击处理
，都需要去更新之前写入的单条数据，
在Kylin这种没有Relpace函数的系统中我们必须把包含对应更新记录的整个Segment数据全部重刷
，但是有了Relpace函数，我们只需要再追加1条新的记录即可。
但是Palo中的Repalce函数有个缺点：无法支持预聚合，
就是说只要你的SQL中包含了Repalce函数，即使有其他可以已经预聚合的Sum，Max指标，也必须现场计算。

一个Key-Value代表HBase中的一行记录，Key-Value由Kylin-Len，Value-Len，Key-Bytes,Value-Bytes 4部分组成。
