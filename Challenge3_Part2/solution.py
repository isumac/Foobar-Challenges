   
def solution(M, F):
    # work backwords finding the number of same operations of either M or F to jump back that number of operations
    # the operations are complementary i.e MMFF and FFMM will give M + 2F,2M + 5F and 5M + 2F, 2M + 1F respectively, where M=1, F=1 gives 3,7 and 7,3
    # therefore the order of the numbers is irrelevant for testing purposes
      
    m = long(M)
    f = long(F)

    totalOps = 0
    while not (m == 1 and f == 1):
        if f <= 0 or m<=0: # should always be >=0 unless one of the inputs is negative
            return "impossible"
        if f == 1: # f will always get to 1 first due swapping of terms
            return str(totalOps + m - 1)
        else:
            totalOps += long(m/f) # will be 0 if f > m and next steps will just swap them
            tempM = m
            m = f
            f = tempM % f # will be tempM if f > tempM 

    return str(totalOps)




