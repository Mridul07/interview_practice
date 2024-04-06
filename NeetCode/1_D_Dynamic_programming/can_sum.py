def can_sum(target,numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False

    for num in numbers:
        remainder = target - num
        if can_sum(remainder, numbers) == True:
            memo[target] = True
            return True
    memo[target] = False
    return False

print(can_sum(7, [2, 3]))
print(can_sum(300, [7, 14]))