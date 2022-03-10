# DNSPod-Easy
DNSPod的DDNS更新。除了简单，什么都没有。

## 如何使用
linux提供了crontab调度器，可以帮助我们定时执行python脚本。
0. 编辑dnspod_easy.py，填写自己的id，token，域名信息
1. 执行`crontab -e`
2. 编辑加入`*/1 * * * * python3 ~/dnspod_easy.py`，如果需要日志输出则执行`*/1 * * * * python3 ~/dnspod_ddns.py >> ~/ddns.log`
3. 享用DNSPod的DDNS自动刷新。
