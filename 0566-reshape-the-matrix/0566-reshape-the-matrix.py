class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Get the dimensions of the original matrix
        m = len(mat)
        n = len(mat[0])
        
        # If the total number of elements doesn't match, the reshape is illegal
        if m * n != r * c:
            return mat
            
        # Initialize the new reshaped matrix with dimensions r x c
        reshaped = [[0] * c for _ in range(r)]
        
        # Fill the new matrix using index math
        for i in range(m * n):
            # Row and column in the original matrix
            orig_r = i // n
            orig_c = i % n
            
            # Row and column in the new matrix
            new_r = i // c
            new_c = i % c
            
            reshaped[new_r][new_c] = mat[orig_r][orig_c]
            
        return reshaped
