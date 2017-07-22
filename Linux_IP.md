# Linux配置IP地址的方法
    1. ifconfig命令临时配置IP地址
    2. setup工具永久配置IP地址(Redhat系列)
    3. 修改网络配置文件
    4. 图形界面配置IP地址

### ifconfig命令
    ifconfig命令:查看与配置网络状态命令(IP和mask)
    ifconfig eth0 102.168.0.200 netmask 255.255.255.0
    #临时设置eth0网卡的IP地址与子网掩码

### ifdown和ifup
    ifdown 网卡设备名
    #禁用该网卡设备
    ifup 网卡设备名
    #启用该网卡设备
### netstat 选项
    选项:
      -t:列出TCP协议端口
      -u:列出UDP协议端口
      -n:不使用域名与服务器,而使用IP地址和端口号
      -l:仅列出在监听状态网络服务
      -a:列出所有网络连接
      -tuln 查询当前开了哪些端口
      -an 查询有谁连接到我的服务器
      -rn 查询网关
      -r 查询路由列表

### route
    route -n
    #查看路由列表(可以查看网关)
    route add default gw ****.****.****.****
    #临时设置网关

>在一台服务器里,连接内网的网卡是不能设置网关的

## 域名解析命令
    nslookup [主机名或IP]
    #进行域名与IP地址解析
    $:nsiookup
      >server
    #查看本机DNS服务器


# 网络测试命令

### ping
    ping [选项] ip或者域名
    #探测指定IP或域名的网络状况
    选项:
      -c 次数: 指定ping包的次数

### telnet (未加密协议)
    telnet [域名或IP] [端口]
    #远程管理与端口探测命令
    telnet 192.168.0.252 80

### traceroute
    traceroute [选项] IP或者域名
    #路由跟踪命令

    选项:
      -n 使用IP,不使用域名,速度更快

### wget命令
    wget http://soft.vpser.net/lnmp/lnmp1.1-full.tar.gz
    #下载命令

### tcpdump命令(抓包)
    tcpdump -i etho -nnX port 21
    选项:
      -i: 指定网卡接口
      -nn: 将数据包中的域名与服务转为IP和端口
      -X: 以十六进制和ASCII码显示数据包内容
      port:指定监听端口
