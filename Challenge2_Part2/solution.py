from itertools import combinations 

def solution(l):
    
    l.sort(reverse=True)
   
    for length in range(len(l),0,-1):
        m = combinations(l, length)
        for a in list(m):
            s = long(''.join([str(n) for n in a]))
            if s % 3 == 0:            
                return s

    return 0        
 




