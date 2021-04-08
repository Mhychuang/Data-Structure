class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        #edge case
        if len(arr) < 3:
            return False
        
        #save some space
        total = sum(arr)
        
        #edge case
        if total % 3:
            return False
        

        targetNum = total / 3    
        sumNum= 0
        count= 0
        
       
        for i in arr:
            sumNum += i
            if sumNum == targetNum:
                #print(sumNum)
                sumNum = 0
                count += 1
                #print (count)
        #case like [0]
        return True if count >= 3 else False
        
        if count >= 2:
            return True
        else:
            return False
        
