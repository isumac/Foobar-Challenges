from itertools import combinations

# if bunnies_required have a key each and num_required - 1 will be missing one key then num_buns - (num_required -1) will have the extra key
# by placing all the keys with these bunnies it will in effect be the plan for distributing the keys

def solution(num_buns, num_required):

    buns = [[] for i in range(num_buns)]
    if num_required == 0:
        return buns
    key = 0
    for bun_combinations in combinations(buns, num_buns - num_required + 1):        
        for bun_keys in bun_combinations:
            bun_keys.append(key)        
        key += 1
    return buns

    