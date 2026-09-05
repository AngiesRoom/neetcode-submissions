class Solution:
    def trap(self, height: List[int]) -> int:

        i = 0
        j = len(height) - 1
        res = 0
        
        if not height:
            return 0
        max_left = height[i]
        max_right = height[j]

        while i < j:
            if max_left < max_right:
                i = i + 1
                max_left = max(max_left, height[i])
                res += max_left - height[i]
            else:
                j = j - 1
                max_right = max(max_right, height[j])
                res += max_right - height[j]
        return res
                

        