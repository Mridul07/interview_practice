class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        total = 0

        for weight in w:
            total += weight
            self.prefix_sum.append(total)
        
        self.total = total

    def pickIndex(self) -> int:
        target = random.uniform(0, self.total)

        l = 0 
        r = len(self.prefix_sum)

        while l<r:
            mid = (l+r) // 2
            if self.prefix_sum[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l

