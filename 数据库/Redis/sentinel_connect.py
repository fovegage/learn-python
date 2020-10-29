from redis.sentinel import Sentinel

# sentinel连接
# 注意password要在连接的时候设置
sentinel = Sentinel([('192.168.43.43', 26379), ('192.168.43.54', 26379), ('192.168.43.59', 26379)], socket_timeout=0.1,
                    password='416798Gao!')
# 返回master节点
master = sentinel.discover_master('mymaster')
print(master)
# 返回slave节点
slaves = sentinel.discover_slaves('mymaster')
print(slaves)
# 使用master节点进行写
master = sentinel.master_for('mymaster', socket_timeout=0.1)
res1 = master.set('test_sentinel', 'hello world')
print(res1)
# 使用slave节点进行读
slave = sentinel.slave_for('mymaster', socket_timeout=0.1)
res2 = slave.get('test_sentinel')
print(res2)
