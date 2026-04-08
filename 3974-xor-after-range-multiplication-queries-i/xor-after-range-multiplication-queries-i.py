class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        

        MOD = 10**9 + 7
        res = nums[:]

        for i in range(len(queries)):
            idx, r, k, v = queries[i]

            while idx <= r:
                res[idx] =(res[idx] * v) % MOD
                idx += k
            
        ans = res[0]
        for i in range(1,len(res)):
            ans ^= res[i]
            
        return ans