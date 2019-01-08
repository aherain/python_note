分布式系统的cap：C一致性，A可用性，P分区容错性 只能满足两项


一致性指“all nodes see the same data at the same time”，即更新操作成功并返回客户端完成后，所有节点在同一时间的数据完全一致。分布式的一致性

可用性指“Reads and writes always succeed”，即服务一直可用，而且是正常响应时间。

分区容错性指“the system continues to operate despite arbitrary message loss or failure of part of the system”，
即分布式系统在遇到某节点或网络分区故障的时候，仍然能够对外提供满足一致性和可用性的服务。