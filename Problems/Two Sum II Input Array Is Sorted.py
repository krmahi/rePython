class solution:
    def TwosumII(self, nums: list, target: int) -> list:
        n = len(nums)
        if n == 2: return [1, 2]

        i, j = 0, n - 1
        while i < j:
            total = nums[i] + nums[j]

            if total > target: j -= 1
            elif total < target: i += 1
            else: return [i + 1, j + 1]