class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_list = [1] * len(nums)
        right_list = [1] * len(nums)

        for i in range(1, len(nums)):
            res_list[i] = nums[i-1] * res_list[i-1]

        for i in range(len(nums) - 2, -1, -1):
            right_list[i] = nums[i+1] * right_list[i+1]
        for i in range(len(res_list)):
            res_list[i] = res_list[i] * right_list[i]
    
        return res_list


            

        
        