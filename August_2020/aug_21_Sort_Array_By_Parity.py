# rainbow sort
# all the elements before curr (exclude) are even numbers
# all the elements between curr (include) and partition (include) are waiting to be explore
# all the elements after partition are odd numbers
# when curr and partition meet each other, the array is all set
# Time complexity : O(n)
# Space complexity : O(1)

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        curr = 0
        partition = len(A)-1
        while curr < partition:
            if A[curr] % 2 == 1:
                A[curr], A[partition] = A[partition], A[curr]
                partition -= 1
            else:
                curr += 1
        return A