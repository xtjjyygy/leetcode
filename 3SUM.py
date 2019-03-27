'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_dict = {}
        result = []

        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1

        pos = [i for i in num_dict if i>0]
        neg = [i for i in num_dict if i<0]
        neg.sort()

        if 0 in num_dict and num_dict[0]>=3:
            result.append([0,0,0])
        for i in pos:
            for j in neg:
                k = -i-j
                if k in num_dict:
                    if (k==i or k==j) and num_dict[k]>=2:#如果k和i或者j中的某个数据相同，则必须要求其出现次数大于2
                        result.append([i,k,j])
                    elif j<k<i: #防止i,j重复
                        result.append([i,k,j])
                    if k<j: #提升循环的速度
                        break
        return result
sol = Solution()
print(sol.threeSum(nums=[-1,0,1,2,-1,-4]))
