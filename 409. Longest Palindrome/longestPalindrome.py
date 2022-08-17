class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        
        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
        
        res = 0
        odd = 0
        
        if len(letters) == 1:
            return letters[s[0]]
        
        for i in letters.values():
            if i > 0 :
                if i % 2 == 0:
                    res += i
                else: 
                    res += i - 1
                    odd += 1
            else:
                odd += 1
        if odd > 0:
            res += 1
            
        return res

# Method 2 from LeetCode Solutions
class Solution:
    def longestPalindrome(self, s):
        ans = 0
        for v in collections.Counter(s).itervalues():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

# ----------------------------------------------------------------------------------------
# Complexity Analysis
# Time Complexity: O(N), where NN is the length of s. We need to count each letter.
# Space Complexity: O(1), the space for our count, as the alphabet size of s is fixed. 
#                   We should also consider that in a bit complexity model, 
#                   technically we need O(logN) bits to store the count values.
# ----------------------------------------------------------------------------------------