class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pre = len(customers)
        max_val = pre
        index = 0 

        for i, c in enumerate(customers):
            if c == 'Y':
                pre += 1
                if max_val < pre:
                    max_val = pre
                    index = i+1
            else:
                pre -= 1 
        return index
        
        