class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
       
        merge = collections.Counter (A[0])     
        
        for i in range (1, len(A)):
            newCount = collections.Counter(A[i])
            
            merge &= newCount
            print (merge)
        
        answer = []
        
        for key in merge.keys():
            num = merge[key]
            # for i in range (num):
            #      answer.append(key)
            answer.extend([key] * merge[key])
            #or 
            #answer = list(merge.elements())

        return answer


# other solution list all the aplphabets 
        alpha = string.ascii_lowercase
        count = {c:0 for c in alpha}
        
        for c in count:
            count[c] = min([word.count(c) for word in A])
            
        
        answer = []
        
        for c in count:
            if count[c] > 0:
                answer.extend([c] * count[c])
                
        return answer
