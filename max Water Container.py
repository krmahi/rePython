class solution:
    def maxAreaOfContainer(self, height: list) -> int:
        n = len(height)

        if n == 2: min(height[0], height[1])

        maxArea, l, r = 0, 0, n - 1
        while l < r:
            distance = r - l
            if height[l] < height[r]:
                minHeight = height[l]
                l += 1
            else:
                minHeight = height[r]
                r -= 1
            area = distance * minHeight
            maxArea = max(maxArea, area)

        return maxArea 