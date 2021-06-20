class Solution(object):
    def reverse(self, x):
        x_str = str(x)

        if x <= -2**31 or x >= 2**31-1:
            return 0
        else:
            if x >= 0:
                ans = int(x_str[::-1])
            else:
                tmp_str = x_str[1:]
                ans_str = "-"+tmp_str[::-1]
                ans = int(ans_str)
        
        if ans <= -2**31 or ans >= 2**31-1:
            return 0
            
        return ans
