# Attop-Auto
一个python实现的至善网刷课软件,主要是理解到了dwr框架下数据的交换
## Environment
> python 版本:3.6
> 系统: mac os
> 依赖: requests

## Usage
    通过`http://www.attop.com/wk/learn.htm?id=48`获得起始和结尾jid
    
    ```
    列如:
    http://www.attop.com/wk/learn.htm?id=48&jid=993
    其中993为起点
    http://www.attop.com/wk/learn.htm?id=48&jid=1013
    1013为终点
    ```
    将数值对应填入

    `` python app.py -u (账号) -p (密码) -s (开始id,列如993) -e (结束id,列如1013) ``
    运行 app.py

## Task
- [ ] 任务一  `自动获取网站页数`
- [x] 任务二  `暂无`

## Attention 
1.  视频时间每次必须间隔为15s
2.  课程评价时间不可短于3S
