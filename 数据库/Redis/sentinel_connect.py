from redis.sentinel import Sentinel

# sentinel连接
sentinel = Sentinel([('192.168.43.43', 26379), ('192.168.43.54', 26379), ('192.168.43.59', 26379)], socket_timeout=0.1)
# 返回master节点
master = sentinel.discover_master('mymaster')
print(master)
# 返回slave节点
slaves = sentinel.discover_slaves('mymaster')
print(slaves)
