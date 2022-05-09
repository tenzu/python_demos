#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

times = input("Lucky draw times: ")
pool = [1, 2, 3, 4, 5]
award = [
    "30 min screen time", "15 min screen time", "No award",
    "15 min study time", "30 min study time"
]
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

a = input("\n")
