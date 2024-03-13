class Solution:
    def pivotInteger(self, n: int) -> int:
        x = [i for i in range(1, n + 1)]
        pivot = len(x) // 2
        left = sum(x[:pivot])
        right = sum(x[pivot:])

        while pivot < n:
            left += x[pivot]
            if left == right:
                return pivot + 1
            right -= x[pivot]
            pivot += 1

        return -1