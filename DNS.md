# DNS

>不配置DNS就不能访问互联网的.

>DNS是Domain Name System的缩写,也就是域名系统的缩写,也称作名称解析

>hosts文件也可以解析域名

>hosts文件的优先级高于DNS解析的

* DNS服务:---层次性----分布式

## 将域名解析为IP地址
    1. 客户机向DNS服务器发送域名查询请求
    2. DNS服务器报告客户机Web服务器的IP地址
    3. 客户机与Web服务器通信

## 域名空间结构(完全合格域名)
* 根域          "  ."
* 顶级域(一级域)    
  >组织域      edu gov com org mil cn mil

  >国家或地区域   cn jp  uk  au  hk

* 二级域  baidu Microsoft IBM...
* 主机名(三级域)  www  NEWS

## DNS查询
     step1. DNS客户机
     step2. 本地域名服务器(如果三天之前访问过会直接在缓存中找到,不然跳转到3)
     step3. 根DNS服务器
     step4. cn
     step5. com.cn
     step6. sina.com.cn
     step7. Web服务器(www.sina.com.cn)

  ![](http://img.blog.csdn.net/20130529002334213)

## DNS查询类型
### 从查询方式上分
    递归查询
      要么做出查询成功响应,要么作出查询失败的响应,一般客户机和服务器之间属递归查询,即当客户机向DNS
      服务器发出请求后,若DNS服务器本身不能解析,则会向另外一个DNS服务器发出查询请求,得到结果后转交
      给客户机

    迭代查询
      服务器收到一次迭代查询回复一次结果,这个结果不一定是目标IP与域名的映射关系,也可以是其他DNS服务器的地址.

### 从查询内容上分
    正向查询由域名查找IP地址
    反向查找由IP地址查找域名
