class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


# Better than the first one
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for char in t:
            if char in char_count:
                char_count[char] -= 1
            else:
                return False
        for count in char_count.values():
            if count != 0:
                return False

        return True

#Better than the second one
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqDict = defaultdict(int)

        for x in s:
            freqDict[x] += 1

        for x in t:
            freqDict[x] -= 1

        for val in freqDict.values():
            if val != 0:
                return False
        return True