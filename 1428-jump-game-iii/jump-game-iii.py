class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        def dfs(i):
            if i < 0 or i >=n or arr[i] < 0:
                return False
            

            if arr[i] == 0:
                return True

            arr[i] = -arr[i]

            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)