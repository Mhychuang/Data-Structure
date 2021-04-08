class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

       
        #need to sort the list. 
        # def sortFunc(x):
        #     return x[0]
        # intervals.sort(key = sortFunc)
        
        intervals.sort(key = lambda x : x[0])
        
        totalLen = len(intervals)
        answer = [intervals[0]]
        
        for  i in range(1, totalLen):
            if answer[-1][1] >= intervals[i][0]:
                # fist numver of the first number set will always be the smallest. 
                #answer[-1]  = [answer[-1][0] , max(answer[-1][1] , intervals[i][1])]
                answer[-1][1]  = max(answer[-1][1] , intervals[i][1])
            else:
                                  
                answer.append(intervals[i])
        
        return answer