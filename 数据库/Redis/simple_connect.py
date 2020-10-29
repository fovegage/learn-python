from redis import StrictRedis

# 初始化客户端
client = StrictRedis(host='127.0.0.1', port='6379')

# 简单字符串设置
client.set('hello', 'world')
