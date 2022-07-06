

# A subsequence maintain relative ordering of elements but may or may not be a contiguous part of an array
# INPUT: array of chars
# OUTPUT: list of list
def allSubsequences_String(arr):
    for i in range(1, (1 << len(arr))):
        op_list = list(f"{i:#0{len(arr)+2}b}".split("b")[1])
        sub = []
        for j in range(len(op_list)):
            if op_list[j] == '1':
                sub.append(arr[j])
        yield sub

# A subsequence maintain relative ordering of elements but may or may not be a contiguous part of an array
# INPUT: array of chars
# OUTPUT: list of list


def allSubsequences_Bits(arr):
    for i in range(1, (1 << len(arr))):
        sub = []
        for j in range(len(arr)):
            if (i & (1 << j)) != 0:
                sub.append(arr[j])
        yield sub

# A subarray is a contiguous part of array and maintains relative ordering of elements
# INPUT: array of chars
# OUTPUT: list of list


def allSubarrays(arr):
    toR = []
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)+1):
            toR.append(arr[i:j])
    return toR

# Objective: Given a number, find out whether its colorful or not.
# Colorful Number: When in a given number, product of every digit of a sub-sequence are different. That number is called Colorful Number. See Example
# Note: using allSubsequences_String algorithm with little adaptation.


def isColorful(n):
    a = list(str(n))
    products = {}
    for i in range(1, (1 << len(a)) - 1):
        op_list = list(f"{i:#0{len(a)+2}b}".split("b")[1])
        prod = 1
        for j in range(len(op_list)):
            if op_list[j] == '1':
                prod *= int(a[j])
        if prod in products:
            return False
        else:
            products[prod] = True
    return True

def isColorful_generator(n):
    a = list(str(n))
    products = {}
    for sub in allSubsequences_String(a):
        prod = 1
        for e in sub:
            prod *= int(e)
        if prod in products:
            return False
        else:
            products[prod] = True
    return True
