class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows=len(matrix)
        cols=len(matrix[0])
        i=0
        j=cols-1

        while i<rows and j>=0:
            if matrix[i][j]==target:
                return True
            elif target < matrix[i][j]:
                j=j-1
            else:
                i=i+1


        return False
        