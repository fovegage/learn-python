# 如何优雅的进行错误重试

> 最近在爬取豆瓣电影所有演员和导演信息的过程中，遇到了一个小问题，目前豆瓣网页端的反爬还是很强的，只有使用代理IP来进行爬取，那么关键的问题来了，即使使用代理IP，也不能100%保证每次请求的不出错误的，那么如何优雅的进行错误重试呢？

## Python异常判断

> Python3版本为我们提供了简单明了的控制语句，即`try...except...else`，别小看`else`的加入，我们可以使用它来干很多事。`else`中的代码只有在没有任何异常发生的情况下才会执行，下一小节我们来看一下，真实业务场景中的使用。

```
try:
    # 逻辑语句
    ...
except:
    # 捕获异常
    ...
else:
    # 未发生异常才执行
    ...
finally:
    ...
    # 后续逻辑
```

## 实际应用

> 由于代理IP不能100%保证使用，我们需要引入一个重试机制，从而保证全量数据可以被爬取下来。这里使用`while`、`continue`、`break`关键字巧妙的实现了一个错误重试功能。

```
import requests


def spider():
    headers = {
        "Host": "movie.douban.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    url = 'https://movie.douban.com/subject/34962956/'
    proxies = {
        'http': 'http://115.211.132.12:8888',
        'https': 'http://115.211.132.12:8888'
    }
    count = 5
    while count > 0:
        try:
            # 注意这里的proxies在每次异常的使用需要重新获取一个
            # 我这里进行了简化
            rep = requests.get(url, headers=headers, proxies=proxies)
        except:
            # 每次异常减1
            count -= 1
            continue
        else:
            # 获取到内容，退出循环
            content = rep.text
            break
    # 继续处理爬取到的内容
    try:
        # 如果重试五次，仍然没有获取到
        handle(content)
    except:
        # 进行异常值记录
        ...
```

## 总结

> 当然大规模爬虫使用Scrapy等开源流行框架是明智的选择，它几乎帮你解决了你所能想到的所有问题，我们只需要简单的配置一下就好了。

- 大家有问题可以留言讨论
- 本次所讲解内容的实质性代码，大家可以加群获取