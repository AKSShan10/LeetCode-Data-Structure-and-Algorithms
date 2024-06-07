count = Counter(magazine)
# for c in ransomNote:
#     if c not in count or count[c] == 0:
#         return False
#     else:
#         count[c] -= 1
# return True
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,'',1)
            else:
                return False
        return True