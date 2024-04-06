def gridTraveller(m, n, memo={}):
    if (m, n) in memo:
        return memo[(m, n)]
    if n == 0 or m == 0:
        return 0
    if n == 1 and m == 1:
        return 1
    memo[(m, n)] = gridTraveller(m-1, n, memo) + gridTraveller(m, n-1, memo)
    memo[(n, m)] = memo[(m, n)]
    return memo[(m, n)]

print(gridTraveller(1, 1))
print(gridTraveller(2, 3))
print(gridTraveller(3, 2))
print(gridTraveller(3, 3))
print(gridTraveller(18, 18))