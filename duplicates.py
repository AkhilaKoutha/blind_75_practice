from typing import List
class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     count = 0 
    #     is_present = False
    #     for key,val in enumerate(nums):
    #         for i,j in enumerate(nums) :
    #             if key == i:
    #                 continue
    #             else:
    #                 if val == j: 
    #                     count = count + 1

    #     if count > 1 :
    #         return True 
    #     else:
    #         return False 

    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        
        
   
if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicate([1,2,3,3]))  # True
    print(sol.hasDuplicate([1,2,3,4]))    # False
