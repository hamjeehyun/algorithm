class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        
        for i in range(len(haystack)):
            tmp_str = haystack[i:i+len(needle)]
            if tmp_str == needle:
                return i
            
        return -1
        