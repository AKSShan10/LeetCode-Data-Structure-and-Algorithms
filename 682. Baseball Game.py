class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        arr = []
        for i in operations:
            if i == 'C':
                arr.pop()
            elif i == 'D':
                temp = 2 * arr[-1]
                arr.append(temp)
            elif i == '+':
                sum = arr[-1] + arr[-2]
                arr.append(sum)
            else:
                arr.append(int(i))
        sum = 0
        for i in arr:
            sum +=i
            #print(sum)
        return sum
'''''
c = Solution()
ops = ["5","2","C","D","+"]
print(c.calPoints(ops))'''