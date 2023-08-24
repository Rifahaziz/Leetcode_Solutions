class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
       
        
        arr=[i for i in str(x)]
        
        if(len(str(x))==1):
            return True
        
        if(len(str(x))%2!=0): #odd
            cback=len(str(x))-1
            cfront=0
            for j in arr:
                if(arr[cfront]==arr[cback]):
                   
                    cfront=cfront+1
                    cback=cback-1
                   
                       
                        
                else:
                    return False
            return True
            
        else: #even
            cback=len(str(x))-1
            cfront=0
            for j in arr:
                if(arr[cfront]==arr[cback]):
                   
                    cfront=cfront+1
                    cback=cback-1
                
                        
                else:
                    return False
            return True
            
