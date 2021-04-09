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
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        #scan from left to i
        for i in range(n):
            output.append(p)
            p = p * nums[i]
        p = 1
        #scan from right to i
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
    
            