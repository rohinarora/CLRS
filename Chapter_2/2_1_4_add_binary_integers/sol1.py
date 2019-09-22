'''
Same as leetcode-
https://leetcode.com/problems/add-binary

Runtime: 40 ms, faster than 72.14% of Python3 online submissions for Add Binary.
Memory Usage: 13.7 MB, less than 5.41% of Python3 online submissions for Add Binary.

'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        carry=0
        result=''
        while (i>=0 or j>=0):
            sum=carry
            if (j>=0):
                sum=sum+int(b[j])
                j=j-1
            if (i>=0):
                sum=sum+int(a[i])
                i=i-1
            result=str(int(sum%2))+result
            carry=int(sum/2)
        if carry!=0:
            result=str(carry)+result
        return result



sol_obj=Solution()


a='1'
b='111'
a='101010101010'
b='101010101010'
a='101110'
b='110'
a='1110'
c=sol_obj.addBinary(a,b)
print (c)
