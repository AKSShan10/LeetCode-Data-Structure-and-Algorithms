'''
Optimal solutions
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s= re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        rev_s=s[::-1]

        if s==rev_s:
            return True
        else:
            return False
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        if len(s) < 0:
            return False
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
