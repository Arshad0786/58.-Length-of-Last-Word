class Solution:
    def lengthOfLastWord(self, s):
        count = 0
        clearTrigger = False
        for i in range(len(s)):
            if s[i] != " ":
                if clearTrigger:
                    count = 0
                    clearTrigger = False
                count = count + 1
            else:
                clearTrigger = True
        return count


# This is one of the most unfun problem I solved on Leetcode.
# Description is not clear enough, which make me having to deal with test cases that isn't mentioned in Description