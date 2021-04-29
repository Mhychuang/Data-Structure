        l = len(nums)
        left, right = 0, l - 1
        res = [0]* l
        cur = l-1
        
        while right >= left:
            if abs(nums[left]) > abs(nums[right]):
                res[cur] = nums[left]**2
                left += 1
            else:
                res[cur] = nums[right]**2
                right -=1
            cur -= 1
        return res
        