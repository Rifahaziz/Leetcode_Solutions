class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = s.split()
        return len(last[-1])


#Runtime : 32ms, Beats 94.26%of users with Python3
