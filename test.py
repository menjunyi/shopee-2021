# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even,
# you have to divide it by 2, otherwise, you have to subtract 1 from it.
# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february




class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            count += 1
        return count
ans = Solution()
print(ans.numberOfSteps(123))