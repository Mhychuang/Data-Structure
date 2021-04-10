class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_ = len(nums)
        #i left
        lList = [1] * len_
        rList = [1] * len_
        
        for i in range(1, len_):
            lList[i] = lList[i - 1] * nums[i - 1]
            
        for i in range(len_ - 2, -1, -1):
            rList[i] = rList[i + 1] * nums[i + 1]
            
        return [lList[i] * rList[i] for i in range(len_)]
    
    ##sol2
    ##Combine step 2 and step 3

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l
        # l -> r         
        for i in range(1, l):
            res[i] = res[i - 1] * nums[i - 1]
        # r -> l         
        productR = 1
        for i in range(l-1, -1, -1):
            res[i] *= productR
            productR *= nums[i]
        return res

    
            