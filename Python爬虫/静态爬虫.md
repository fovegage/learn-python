# 本篇介绍静态爬虫的使用

> 我们都知道

### 安装Aria2

- 安装

```
sudo apt install -y aria2 
```
- 创建文件夹并添加配置信息

```
mkdir -p ~/.config/aria2/ 
vim ~/.config/aria2/aria2.config
```
- 添加配置信息

```
#后台运行
daemon=true
#用户名
#rpc-user=user
#密码
#rpc-passwd=passwd
#设置加密的密钥
rpc-secret=secret
#允许rpc
enable-rpc=true
#允许所有来源, web界面跨域权限需要
rpc-allow-origin-all=true
#是否启用https加密，启用之后要设置公钥,私钥的文件路径
#rpc-secure=true
#启用加密设置公钥
#rpc-certificate=/home/pi/.config/aria2/example.crt
#启用加密设置私钥
#rpc-private-key=/home/pi/.config/aria2/example.key
#允许外部访问，false的话只监听本地端口
rpc-listen-all=true
#RPC端口, 仅当默认端口被占用时修改
#rpc-listen-port=6800
#最大同时下载数(任务数), 路由建议值: 3
max-concurrent-downloads=5
#断点续传
continue=true
#同服务器连接数
max-connection-per-server=5
#最小文件分片大小, 下载线程数上限取决于能分出多少片, 对于小文件重要
min-split-size=10M
#单文件最大线程数, 路由建议值: 5
split=10
#下载速度限制
max-overall-download-limit=0
#单文件速度限制
max-download-limit=0
#上传速度限制
max-overall-upload-limit=0
#单文件速度限制
max-upload-limit=0
#断开速度过慢的连接
#lowest-speed-limit=0
#验证用，需要1.16.1之后的release版本
#referer=*
#文件保存路径, 默认为当前启动位置(我的是外置设备，请自行坐相应修改)
dir=/media/share
#文件缓存, 使用内置的文件缓存, 如果你不相信Linux内核文件缓存和磁盘内置缓存时使用, 需要1.16及以上版本
#disk-cache=0
#另一种Linux文件缓存方式, 使用前确保您使用的内核支持此选项, 需要1.15及以上版本(?)
#enable-mmap=true
#文件预分配, 能有效降低文件碎片, 提高磁盘性能. 缺点是预分配时间较长
#所需时间 none < falloc ? trunc << prealloc, falloc和trunc需要文件系统和内核支持
file-allocation=prealloc
#不进行证书校验
check-certificate=false
#保存下载会话
save-session=/home/pi/.config/aria2/aria2.session
input-file=/home/pi/.config/aria2/aria2.session
#断电续传
save-session-interval=60
```

- 创建共享文件夹

```
mkdir /media/share
```

- 创建会话信息

```
touch /home/pi/.config/aria2/aria2.session
```

- 启动 Aria2

```
aria2c --conf-path=/home/pi/.config/aria2/aria2.config
ps aux|grep aria2
```

### 设置Aria2自启动

- 创建文件

```
sudo vim /lib/systemd/system/aria.service
```

- 添加配置信息

```
[Unit]
Description=Aria2 Service
After=network.target

[Service]
User=pi
Type=forking
ExecStart=/usr/bin/aria2c --conf-path=/home/pi/.config/aria2/aria2.config

[Install]
WantedBy=multi-user.target
```

- 相关命令

```
重新载入服务，并设置开机启动 
sudo systemctl daemon-reload 
sudo systemctl enable aria 
查看aria服务状态 
sudo systemctl status aria 
启动，停止，重启aria服务 
sudo systemctl（start、stop、restart） aria
```

### 添加 Aria2 Web管理界面

- 安装 Nginx

```
# 安装git和nginx
sudo apt install -y git nginx
```

- 安装 Aria2 Web

```
# 下载aira-ng
wget https://github.com/mayswind/AriaNg/releases/download/1.1.1/AriaNg-1.1.1.zip -O aira.zip
# 解压
unzip aira.zip -d aira
# 将aira-ng放到nginx的/var/www/html/目录下，然后设置开机启动nginx
sudo mv aira-ng /var/www/html/
sudo systemctl enable nginx
```

- 访问

```
浏览器输入：http://192.168.2.196/aira  # 根据路由器分配的IP进行访问
```

![微信图片_20190623212800.png](https://i.loli.net/2019/06/23/5d0f82e9a06b330226.png)

### 下载百度网盘内容

- 待更新

### 下载速度慢的问题

- 添加 bt-tracker ([bt-tracker 最新地址](https://github.com/ngosang/trackerslist))

```
# 进入aira2配置
vim ~/.config/aria2/aria2.config
# 添加如下(自行用“,”分隔每个tarck)
bt-tracker=udp://tracker.coppersurfer.tk:6969/announce,udp://tracker.open-internet.nl:6969/announce,udp://tracker.skyts.net:6969/announce,udp://tracker.piratepublic.com:1337/announce,udp://tracker.opentrackr.org:1337/announce,udp://9.rarbg.to:2710/announce,udp://retracker.coltel.ru:2710/announce,udp://pubt.in:2710/announce,udp://public.popcorn-tracker.org:6969/announce,udp://z.crazyhd.com:2710/announce,udp://wambo.club:1337/announce,udp://tracker4.itzmx.com:2710/announce,udp://tracker1.wasabii.com.tw:6969/announce,udp://tracker.zer0day.to:1337/announce,udp://tracker.xku.tv:6969/announce,udp://tracker.vanitycore.co:6969/announce,udp://ipv4.tracker.harry.lu:80/announce,udp://inferno.demonoid.pw:3418/announce,udp://open.facedatabg.net:6969/announce,udp://mgtracker.org:6969/announce
```

- 打开 DMCA 服务

```
# 进入aira2配置
vim ~/.config/aria2/aria2.config
# 添加如下
enable-dht=true
bt-enable-lpd=true
enable-peer-exchange=true
```

### 其他WebUI

YAAW: [下载地址](https://github.com/binux/yaaw)

Webui-aria2：[下载地址](https://github.com/ziahamza/webui-aria2)

Glutton：[下载地址](https://github.com/NemoAlex/glutton)

### 参考文档

[安装使用aria2下载百度网盘内容](https://www.cnblogs.com/loveyouyou616/p/10361397.html)

[BT网站](https://www.torrentdownloads.me/)

[解决Aria2 BT下载速度慢没速度的问题](http://www.senra.me/solutions-to-aria2-bt-metalink-download-slowly/)

[树莓派3B+ 远程下载服务器（Aria2）](https://blog.csdn.net/kxwinxp/article/details/80288006)

[下载工具系列——Aria2 (几乎全能的下载神器)](http://www.senra.me/awesome-downloader-series-aria2-almost-the-best-all-platform-downloader/)