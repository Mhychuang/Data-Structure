class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        remainderCount = [0] * 60
        
        for t in time:
            #how much this time left. 
            #take 100 as example, it has 40 left, meaning it can offer 40 
            t %= 60
            
            #for but it needs 20 more to be able to make it to 60
            # it check previously how many guys has 20 left
            howMany = remainderCount[(60-t)%60]
            ans += howMany
            # mark on the list saying i have 40 more. 
            remainderCount[t] += 1
            
        return ans