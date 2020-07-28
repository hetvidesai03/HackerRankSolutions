#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    l=list(set(ar))
    socks=[]
    for i in l:
        socks.append([i, ar.count(i)])
    print(socks)
    
    count=0
    for item in socks:
        if item[1]>1:
            count+=int(item[1]/2)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
