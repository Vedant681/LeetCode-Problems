class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_delete = arr[0]
        one_delete = float(-inf)
        answer = arr[0]

        for i in range(1, len(arr)):
            x = arr[i]
            one_delete = max(one_delete + x, no_delete)
            no_delete = max(no_delete + x, x)
            answer = max(answer, one_delete, no_delete)
        
        return answer

        