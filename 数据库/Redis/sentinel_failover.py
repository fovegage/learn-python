from redis.sentinel import Sentinel
import time
from functools import wraps
import logging

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)


def redis_single(func):
    instance = {}

    @wraps(func)
    def warped(*args, **kwargs):
        if func not in instance:
            instance[func] = func(*args, **kwargs)
        return instance[func]

    return warped


# sentinel连接


# 注意password要在连接的时候设置
# 需要使用单列模式，edis连接池最大连接数默认设置为10000 maxclients
@redis_single
def single_sentinel():
    # 不会新创建实列 会一直动态修改一个实例对象的赋值
    # 如果直接用for 就是不断的进行创建对象
    sentinel = Sentinel([('192.168.43.43', 26379), ('192.168.43.54', 26379), ('192.168.43.59', 26379)],
                        socket_timeout=0.1,
                        password='416798Gao!')
    return sentinel.master_for('mymaster', socket_timeout=0.1)


master = single_sentinel()

# 返回master节点
i = 0
for count in range(11000, 30000):
    key = f'key-{count}'
    value = f'value-{count}'
    if count % 100 == 0:
        logging.info(f'第{i}次个100日志')
    try:
        logging.info(id(master))
        master.set(key, value)
        time.sleep(0.001)
    except Exception as e:
        logging.info(id(master))
        logging.error(e)
        logging.info('集群故障')
        continue
    finally:
        i += 1
