class Solution(object):
    def isValid(self, s):
        ch_list = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                ch_list.append(i)
                continue
            else:
                if len(ch_list) == 0:
                    return False
                a = ch_list.pop()
                if i == ")" and a != "(":
                    return False
                elif i == "}" and a != "{":
                    return False
                elif i == "]" and a != "[":
                    return False 
                else:
                    continue
        if len(ch_list) != 0:
            return False
        return True