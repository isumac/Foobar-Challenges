
def solution(l,t):

    runningtotal = 0
    for i in range(0, len(l)):
            
        runningtotal += l[i]
        if runningtotal == t:
            return [0, i]
        
        if runningtotal > t:                        
            result = solution(l[1:len(l)], t)
            return[1 + result[0], 1 + result[1]]           
            
    return [-1,-1] 



