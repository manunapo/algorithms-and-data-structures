#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#
from collections import deque
def bfs(n, m, edges, s):
    toR = [-1 for x in range(n)]
    q = deque()
    q.append((s,0))
    toR[s-1] = 0
    while len(q) > 0:
        node,units = q.popleft()
        for fr,to in edges:
            if node == fr and (toR[to - 1] == -1):
                q.append((to,units + 6))
                toR[to - 1] = units + 6
            elif node == to and (toR[fr - 1] == -1):
                q.append((fr,units + 6))
                toR[fr - 1] = units + 6
    return [x for x in toR if x != 0]
    
        
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
