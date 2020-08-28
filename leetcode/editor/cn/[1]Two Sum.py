# Given an array of integers, return indices of the two numbers such that they a
# dd up to a specific target. 
# 
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice. 
# 
#  Example: 
# 
#  
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#  
#  Related Topics 数组 哈希表 
#  👍 8871 👎 0


from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.hash = dict()
        self.res = dict()

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.hash = dict(zip(nums, [i for i in range(len(nums))]))
        for idx, num in enumerate(nums):
            if target - num in self.hash and self.hash[target-num] != idx:
                return [idx, self.hash[target - num]]
        return []


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([3, 2, 4], 6))