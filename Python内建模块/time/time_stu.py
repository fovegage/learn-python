# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 11:42
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : time_stu.py
# @Software: PyCharm

import time

'altzone', 'asctime', 'clock', 'ctime', 'daylight', 'get_clock_info', \
'gmtime', 'localtime', 'mktime', 'monotonic', 'perf_counter', 'process_time', \
'sleep', 'strftime', 'strptime', 'struct_time', 'time', 'timezone', 'tzname'

print(time.altzone)  # 格林威治西部的夏令时地区的偏移秒数
print(time.daylight)
print(time.timezone)
print(time.tzname[0].encode('latin-1').decode('gbk'))   # 中国夏令时

# int tm_sec; /* 秒 – 取值区间为[0,59] */
# int tm_min; /* 分 - 取值区间为[0,59] */
# int tm_hour; /* 时 - 取值区间为[0,23] */
# int tm_mday; /* 一个月中的日期 - 取值区间为[1,31] */
# int tm_mon; /* 月份（从一月开始，0代表一月） - 取值区间为[0,11] */
# int tm_year; /* 年份，其值等于实际年份减去1900 */
# int tm_wday; /* 星期 – 取值区间为[0,6]，其中0代表星期天，1代表星期一，以此类推 */
# int tm_yday; /* 从每年的1月1日开始的天数 – 取值区间为[0,365]，其中0代表1月1日，1代表1月2日，以此类推 */
# int tm_isdst; /* 夏令时标识符，实行夏令时的时候，tm_isdst为正。不实行夏令时的时候，tm_isdst为0；不了解情况时，tm_isdst()为负。

# r若不指定 则按 localtime()  进行
t = (2018, 5, 27, 1, 5, 27, 6, 147, -1)
print(time.asctime(t))
# 参数 localtime()
print(time.asctime())

# 格式化时间戳为本地的时间   24小时制
print(time.localtime())

# 若不知道 seconds 则 使用 time.time()  12小时制
print(time.gmtime())

# 计算 call 开始 cpu 的执行时间
print(time.clock())

# 参数秒
print(time.ctime())

# 获取指定时钟的信息
# 'clock': time.clock()
# 'monotonic': time.monotonic()
# 'perf_counter': time.perf_counter()
# 'process_time': time.process_time()
# 'time': time.time()
print(time.get_clock_info('clock'))

t = (2019, 5, 27, 1, 5, 27, 6, 147, -1)
# 接收struct_time对象作为参数 返回 seconds
print(time.mktime(t))

print(time.monotonic())
print(time.perf_counter())
print(time.process_time())

# 延时
# print(time.sleep(2))

# 格式化时间  将 struct_time  转化为 str  未指定 localtime
# 2019-04-02 15:47:24
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# str -> struct_time
struct_time = time.strptime("30 Nov 18", "%d %b %y")
print(struct_time)
struct_time1 = time.strptime('2018-07-11 17:41:20', '%Y-%m-%d %H:%M:%S')
print(struct_time1)

# 秒
print(time.time())

