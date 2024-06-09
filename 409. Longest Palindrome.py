class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter = {}
        for char in s:
            if char not in letter:
                letter[char] = 1
            else:
                letter[char] += 1
        res, odd = 0, 0
        if len(letter) == 1:
            return letter[s[0]]
        for i in letter.values():
            if i > 1:
                if i % 2 == 0:
                    res += i
                else:
                    res += (i - 1)
                    odd += 1
            else:
                odd += 1
        if odd > 0:
            res += 1
        return res
