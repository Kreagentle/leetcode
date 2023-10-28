class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic = {}
        left, right, maxim = 0, 0, 0

        while right < len(s):
            dic[s[right]] = dic.get(s[right], 0) + 1

            while dic[s[right]] > 1:
                    dic[s[left]] -= 1
                    left += 1

            if (right - left + 1) > maxim:
                maxim = right - left + 1

            right += 1

        return maxim