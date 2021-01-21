import time

def solution(start, length):
   
    result = 0

    for i in range(0 , length):
        rangeStart = start + (i * length)

        ## exploits the fact that (4^5^6) === (1^2^3^4^5^6) ^ (1^2^3) as n ^ n = 0 so the terms cancel out
        result  ^= calcXor(rangeStart + length - i - 1) ^ calcXor(rangeStart - 1)

    return result

## uses the fact XOR repeats in a patterm every 4 bits  
def calcXor(n):

    return [n, 1, n+1, 0][n % 4]  
 


