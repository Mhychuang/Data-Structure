class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        i=0
        while i<len(arr):
            if arr[i]==0:
                arr.pop() # O(1)
                arr.insert(i+1,0) # O(N)
                i+=2
            else:i+=1
            