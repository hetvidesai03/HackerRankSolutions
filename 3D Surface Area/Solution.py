#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the surfaceArea function below.
def surfaceArea(A):
    area = 2*H*W
    def check(i,j):
        return A[x+i][y+j] if 0<=x+i<H and 0<=y+j<W else 0
    xi=[0,0,1,-1]
    yi=[1,-1,0,0]

    for x in range(H):
        for y in range(W):
            for i,j in zip(xi,yi):
                area+= max(0,A[x][y]- check(i,j))

    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
