# Attop-Auto
一个python实现的至善网刷课软件,主要是理解到了dwr框架下数据的交换
## environment
> python 版本:3.6
> 系统: mac os
> 依赖: requests

## usage
1.  通过`http://www.attop.com/wk/learn.htm?id=48`获得起始和结尾jid
    
    ```
    列如:
    http://www.attop.com/wk/learn.htm?id=48&jid=993
    其中993为起点
    http://www.attop.com/wk/learn.htm?id=48&jid=1013
    1013为终点
    ```
将数值对应填入
    
    ```
    if __name__ == "__main__":
    username = '##########'
    password = '##########'
    start = 0
    end = 0
    main()
    ```
    
2.  对应填入账号(username),密码(password)
3.  运行 app.py

## Task
- [ ] 任务一  `自动获取网站页数`
- [x] 任务二  `暂无`

## attention 
1.  视频时间每次必须间隔为15s,不然返回错误
2.  课程评价时间不可短于3S


    







