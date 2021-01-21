import re
import math
from textwrap import wrap

def solution(search_string):
    factors = factorise(len(search_string))
    sub = search_string[0:len(set(search_string))]
    for factor in factors:   
        substring = search_string[0:factor["factor1"]]

        totalSubStrings = 0
        for i in range(0, len(search_string), factor["factor1"]):
            if search_string[i : i + factor["factor1"]] == substring:
                totalSubStrings +=1
        
        if totalSubStrings == factor["factor2"]:
            return factor["factor2"]

        if len(re.findall(substring, search_string)) == factor["factor2"]:
            return factor["factor2"]    

    return 0

def factorise(x):
    factors = []
    for i in range(1,x + 1):
        if x % i == 0:
            factors.append({"factor1" : i, "factor2" : int(x/i)})
    
    return factors

print(solution('abcabcabcabc'))
print (solution("bcabcabcabca"))
print(solution("bccbaabccbaa"))
print(solution("ccbaabccbaab"))
print(solution("cbaabccbaabc"))
