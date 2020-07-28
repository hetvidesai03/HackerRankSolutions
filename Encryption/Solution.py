#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    
    data_length= len(s)
    sr= math.sqrt(data_length)
    row=int(math.floor(sr))
    column=int(math.ceil(sr))
    l=[]
    decrypted_answer=""
    for i in range(0, data_length, column):  
        l.append(s[i:i + column])
    
    last= l[-1]
    if(len(last) is not column):
        for i in range(0,column-len(last)):
            l[-1]+=(" ")
    
    for y in range(0,column):
        
        decrypted_answer+= "".join([item[y] for item in l]).strip()
        decrypted_answer+=" "
    return decrypted_answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
