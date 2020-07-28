#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count=0
    arr=[]
    valley_count=0
    for i in s:
        if i=='U':
            count+=1    
        else:
            count-=1
        arr.append(count)
    if arr[0]<0:
        valley_count+=1
    for i in range(1,len(arr)):
        
        if arr[i]<0 and arr[i-1]==0:
            valley_count+=1
    
    return valley_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
