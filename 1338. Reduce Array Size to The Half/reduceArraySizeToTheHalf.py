class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        # First method to get arrCount:
        arrCount = {}
        for number in arr:
            if number in arrCount:
                arrCount[number] += 1
            else:
                arrCount[number] = 1
                
        # Second method to get the arrCount:
        # arrCount = collections.Count(arr)
        
        # Sorting the arrCount from Big to Small
        sortedArrCount = sorted(arrCount.values(), reverse=True)
        
        limit = len(arr) // 2
        arrTotalCount = len(arr)
        res = 0
        
        for number in sortedArrCount:
            if arrTotalCount > limit:
                arrTotalCount -= number
                res += 1
            else:
                break
        return res