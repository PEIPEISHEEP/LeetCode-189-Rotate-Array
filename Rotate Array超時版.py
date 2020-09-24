class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=len(nums)-1
        p=l
        save=0
        while k>len(nums):
            k-=len(nums)
        for j in range(k):
            save=nums[l]
            for i in range(len(nums)):
                p -=1
                if p==(-1):
                    nums[0]=save
                else:
                    nums[l]=nums[p]
                l -=1
            l=len(nums)-1
            p=l