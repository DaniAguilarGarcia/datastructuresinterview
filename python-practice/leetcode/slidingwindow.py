#longest substring o(2n)

class Solution:
    def lenofSub(self, s: str) -> int:
        chars = [0] * 128
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(1)] -=1
                left += 1
            res = max(res, right - left +1)

            right += 1
        return res

    #opti
class Solution:
    def lenOfSub(self, s: str) -> int:
        n = len(s)
        ans = 0
        #mp sotres the current index of a char
        mp = {}

        i = 0
        #try to extend the range [i,j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(ans, j - i + 1)
            mp[a[j]] = j + 1
        return ans
        

    
