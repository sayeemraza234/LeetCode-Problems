# The guess API is already defined for you.
# def guess(num):

class Solution:
    def guessNumber(self, n):
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2

            result = guess(mid)

            if result == 0:
                return mid
            elif result == 1:
                left = mid + 1
            else:
                right = mid - 1