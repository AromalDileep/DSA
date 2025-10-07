class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        nums.sort()  # sort to handle duplicates
        visited = [False] * len(nums)
        
        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                # skip duplicates
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                
                sol.append(nums[i])
                visited[i] = True
                backtrack()
                visited[i] = False
                sol.pop()
        
        backtrack()
        return res
