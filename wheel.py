#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
times = input("Lucky draw times: ")
pool = [1, 2, 3, 4, 5]
reward = ["30分钟屏幕时间", "15分钟屏幕时间", "无奖励", "学习15分钟", "学习30分钟"]
i = 1
while i <= int(times):
    j = random.choice(pool)
    print("This time the lucky number is:", j)
    print(reward[j-1])
    i += 1

#---########
# ---import random
# ---rewardDict = {
# ---    '一等奖':(0,0.08),
# ---    '二等奖':(0.08,0.3),
# ---    '三等奖':(0.3,1.0)
# ---}
# ---
# ---def rewardFun():
#---    """用户得奖等级"""
# ---    #生成一个0～1之间的随机数
# ---    num = random.random()
# ---    #判断随机转盘转的是几等奖
# ---    for k,v in rewardDict.items():
# ---        if v[0] <= num < v[1]:
# ---            return k
# ---
# ---print("黄子峻小朋友本次获得：",rewardFun())
# ---resultDict = {}
# ---
# ---for i in range(1000):
# ---    res = rewardFun()
# ---    if res not in resultDict:
# ---        resultDict[res] = 1
# ---    else:
# ---        resultDict[res] += 1
# ---
# ---for k,v in resultDict.items():
#---    print(k,'------>',v)
# ---
