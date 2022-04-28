#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

times = input("Lucky draw times: ")
pool = [1, 2, 3, 4, 5]
award = ["30 min. screen time", "15 min. screen time", "No award", "15 min. study time", "30 min. study time"]
i = 1
j = len(pool)
while i <= int(times):
    k = random.choice(pool)
    print("This time the lucky number is:", k)
    print(award[k - 1])
    if k <= j:
        j = k
    i += 1
print("\nThe best award is:", award[j - 1])

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
