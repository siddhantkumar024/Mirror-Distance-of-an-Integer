class Solution:
    def mirrorDistance(self, n: int) -> int:
        rv=n
        rev=0
        while rv>0:
            d=rv%10
            rev=rev*10+d
            rv=rv//10
        
        return abs(n-rev)

        
