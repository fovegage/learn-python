from collections import namedtuple

Stock = namedtuple("User", ['uid', 'username', 'password'])
info = '1', "Gage", "123456"
s = Stock(*info)
print(s)
s1 = s._replace(password='111111')
print(s1)