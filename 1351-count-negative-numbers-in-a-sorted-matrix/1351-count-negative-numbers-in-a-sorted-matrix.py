class Solution:
    def countNegatives(self, grid):
        count = 0

        for row in grid:
            left = 0
            right = len(row) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1

            count += len(row) - left

        return count