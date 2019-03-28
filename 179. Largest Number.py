'''
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
'''

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        if max(nums) == 0:
            return '0'
        nums = list(map(str, nums))
        from functools import cmp_to_key
        nums.sort(key=cmp_to_key(lambda a, b: int(a + b) - int(b + a)), reverse=True)
        return ''.join(nums)

sol = Solution()
print(sol.largestNumber(nums=[3,30,5,9,34]))
