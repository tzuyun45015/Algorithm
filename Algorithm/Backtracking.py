class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            backtrack(i+1)
        
        # don't forget empty subset
        backtrack(0)
        return res

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择

        
