class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for i in range(len(nums)):
            num = nums[i]
            print (num)
            if num not in dict_:
                dict_[target - num] = i
                print (dict_)
            else:
                return [dict_[num], i]
        print (dict_)
                