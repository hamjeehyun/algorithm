import re

class Solution(object):
    def isPalindrome(self):
        s = self.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]
