from redis import StrictRedis

# 初始化客户端
client = StrictRedis(host='127.0.0.1', port='6379')

# 简单字符串设置
print(client.get('test'))

# '0100111000100101'

# 0b100 111101 100000

# 11100100 10111101 10100000


# 0b1 1111 011000 000010

# 111011111001100010000010
# 111010011010101110011000
for index, item in enumerate('111001001011110110100000'):
    print(index, item)
    client.setbit('test-8', index, int(item))
