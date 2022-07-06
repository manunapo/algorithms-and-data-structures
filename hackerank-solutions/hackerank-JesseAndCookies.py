#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#
import heapq as hq

def recursive(k, H, i):
    min1 = hq.heappop(H)
    if min1 >= k:
        return i
    if len(A) == 0:
        return -1
    prod = min1 + 2*hq.heappop(H)
    hq.heappush(H, prod)
    return recursive(k,H, i+1)
        
            
def cookies(k, A):
    hq.heapify(A)
    #return recursive(k, A,0)

    ops = 0
    while True:
        min1 = hq.heappop(A)
        if min1 >= k:
            return ops
        if len(A) == 0:
            return -1
        prod = min1 + 2*hq.heappop(A)
        hq.heappush(A,prod)
        ops += 1
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
