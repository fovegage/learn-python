from pathlib import Path
import pathlib

# 实例化Path,路径可以是不存在的
p = Path('E:\study')
# print([x for x in p.iterdir() if x.is_dir()])

# 输出实例化的绝对路径
print(p.absolute())


# 判断路径是否存在
print(p.exists())

#
print(p.expanduser())

# 返回所属分组，windows不支持
# print(p.group())
