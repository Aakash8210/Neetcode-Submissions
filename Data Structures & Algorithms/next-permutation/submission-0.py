class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)  # Size of the given array

        # To store the index of the first smaller element from right
        ind = -1

        # Find the first index from the end where nums[i] < nums[i+1]
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break

        ''' If no such index exists, array is in descending order
            So, reverse it to get the smallest permutation '''
        if ind == -1:
            nums.reverse()
            return

        # Find the element just greater than nums[ind] from the end
        for i in range(n-1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]  # Swap with nums[ind]
                break

        # Reverse the right half to get the next smallest permutation
        nums[ind+1:] = reversed(nums[ind+1:])
        return
        