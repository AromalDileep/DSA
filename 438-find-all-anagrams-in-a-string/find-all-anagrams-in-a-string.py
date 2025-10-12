class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Lengths of both strings
        len_p = len(p)
        len_s = len(s)
        # If p is longer than s, there can't be any anagram
        if len_p > len_s:
            return []
        # Step : Create frequency count of characters in p
        # Example: if p = "abc" -> p_count = {'a':1, 'b':1, 'c':1}
        p_count = Counter(p)
        # Step : Initialize the first window in s with same size as p
        # Example: if s = "cbaebabacd" and p = "abc"
        # window_count = {'c':1, 'b':1, 'a':1}
        window_count = Counter(s[:len_p])
        # This will hold the starting indices of all anagrams
        res = []
        # Step : If the very first window is already an anagram, store index 0
        if window_count == p_count:
            res.append(0)
        # Step : Now slide the window across string s
        # We'll move one character at a time
        for i in range(len_p, len_s):
            # Add new character (the one coming into the window)
            window_count[s[i]] += 1
            # Remove the old character (the one leaving from the left side)
            left_char = s[i - len_p]
            window_count[left_char] -= 1
            # If count of a character becomes 0, remove it to keep comparison clean
            if window_count[left_char] == 0:
                del window_count[left_char]
            # If after the shift, both counters match — it's an anagram!
            if window_count == p_count:
                # Append starting index of the current window
                res.append(i - len_p + 1)
        # Step : Return all starting indices where anagrams were found
        return res
