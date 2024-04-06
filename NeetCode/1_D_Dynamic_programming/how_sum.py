def how_sum(target, numbers, memo=None):
    memo = {} if memo is None else memo
    
    if target in memo:
        return memo[target]
    
    if target == 0:
        return []
    
    if target < 0:
        return None
    
    for num in numbers:
        remainder = target - num
        remainder_result = how_sum(remainder, numbers, memo)

        if remainder_result is not None:
            remainder_result.append(num)
            memo[target] = remainder_result
            # memo[target] = remainder_result + [num]
            return remainder_result
    
    memo[target] = None
    return None



# Test the function
print(how_sum(7, [2, 3]))  # Output: [3, 2, 2]
print(how_sum(7, [5, 3, 4, 7]))  # Output: [4, 3]
print(how_sum(7, [2, 4]))  # Output: None
print(how_sum(8, [2, 3, 5]))  # Output: [2, 2, 2, 2]
print(how_sum(300, [7, 14]))  # Output: None