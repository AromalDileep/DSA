class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        pos_idx = {}
        for idx, pos in enumerate(order):
            pos_idx[pos] = idx
        
        return sorted(friends, key=lambda x:pos_idx[x]) 