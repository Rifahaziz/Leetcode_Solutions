class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        vals = {'I':1, 'V':5, 'X':10,'L':50,'C':100, 'D':500, 'M':1000}
        sum=0
        i=0
        while i<len(s):
            if(i<len(s)-1):
       
                if(vals[s[i]]<vals[s[i+1]]):
                    sum=sum+vals[s[i+1]] - vals[s[i]]
                    i=i+2
                else:
                    sum=sum+vals[s[i]]
                    i=i+1
            else:
               sum=sum+vals[s[i]]
               i=i+1
            
        return sum
