def best_sum(target, numbers, memo=None):
    memo = {} if memo == None else memo

    if target in memo:
        return memo[target]
    
    if target == 0: 
        return []
    
    if target < 0: 
        return None

    best_sum_res = None

    for num in numbers:
        remainder = target - num
        remainder_result = best_sum(remainder, numbers, memo)

        if remainder_result is not None:
            comb = remainder_result + [num]
            # print(remainder_result)
            if (best_sum_res is None or len(comb) < len(best_sum_res)):
                best_sum_res = comb

        
    memo[target] = best_sum_res
    return best_sum_res



# Test the function
print(best_sum(8, [2, 3])) 
print(best_sum(7, [5, 3, 4, 7]))  
print(best_sum(7, [2, 4]))  
print(best_sum(8, [2, 3, 5]))  
print(best_sum(200, [1, 7, 14, 25]))  