> 匹配流程

- 字符串前面加 r 表示原生
- 使用 compile() 函数将正则表达式的字符串形式编译为一个 Pattern 对象
- 通过 Pattern 对象提供的一系列方法对文本进行匹配查找，获得匹配结果，一个 Match 对象。
- 最后使用 Match 对象提供的属性和方法获得信息，根据需要进行其他的操作

> 匹配规则

[![5.2.png](https://i.loli.net/2019/06/20/5d0b2066063bf98751.png)](https://i.loli.net/2019/06/20/5d0b2066063bf98751.png)


> 贪婪、非贪婪模式

[请参阅](https://blog.csdn.net/lxcnn/article/details/4756030)

> 注意

- re.I 表示忽略大小写
- A = ASCII
- I = IGNORECASE
- L = LOCALE
- U = UNICODE
- M = MULTILINE
- S = DOTALL
- X = VERBOSE
- T = TEMPLATE