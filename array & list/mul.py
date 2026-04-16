
class Solution:
    def getTable(self,n):
        for i in range(1,11):
            result = n*i
            print(result, end = " ")

m=Solution()

m.getTable(68)