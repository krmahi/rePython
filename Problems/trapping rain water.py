# two arrays: time -> O(n), space -> O(n)
class solution:
    def traprainwater(self, height: list) -> int:
        n = len(height)
        max_el = max(height)

        left_array = []
        right_array = []
        left_max, right_max, count = 0

        for i in range(n - 1):
            if height[i] == max_el:
                left_array.extend([max_el] * n - i)
                break
            left_max = max(left_max, height[i])
            left_array.append(left_max)
        
        for i in range(n - 1, -1, -1):
            if height[i] == max_el:
                right_array.extend([max_el] * i + 1)
                break
            right_max = max(right_max, height[i])
            right_array.append(right_max)
        right_array.reverse()

        for i in range(n - 1):
            count += min(left_array[i], right_array[i]) - height[i]
        
        return count
    
# two pointer: time -> O(n), space -> O(1)
class solution:
    def traprainwater(self, height: list) -> int:
        n = len(height)
        i, j = 0, n - 1
        max_left, max_right = height[i], height[j]

        res = 0
        while i < j:
            if max_left <= max_right:
                i += 1
                max_left = max(max_left, height[i])
                res += max_left - height[i]
            else:
                j -= 1
                max_right = max(max_right, height[j])
                res += max_right - height[j]
        
        return res