class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        #print(size)
        c = 0
        i = 0
    
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
                c += 1
           
            else:
                i += 1

        nums.sort()
        #print("length",len(nums))
       
        #k=size-c

        return len(nums)

#Runtime: 110 ms
#Memory Usage: 14.4 MB
