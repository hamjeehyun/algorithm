class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        reverse_x = x_str[::-1]
        
        if reverse_x == x_str:
            return True
        else:
            return False