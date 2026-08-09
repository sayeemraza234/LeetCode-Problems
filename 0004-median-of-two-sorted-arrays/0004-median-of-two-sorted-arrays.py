class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array to optimize the binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # Handle edge cases where partition is at the extreme ends
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Check if we have found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If total length is odd, median is the max of the left elements
                if (x + y) % 2 == 1:
                    return float(max(maxLeftX, maxLeftY))
                # If total length is even, median is average of max left and min right
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                    
            # We are too far on the right side for partitionX. Go on left side.
            elif maxLeftX > minRightY:
                high = partitionX - 1
                
            # We are too far on the left side for partitionX. Go on right side.
            else:
                low = partitionX + 1
                
        raise ValueError("Input arrays are not sorted or are invalid.")