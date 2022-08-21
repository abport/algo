# Complexity ----------------------------------------------------------
# Time: O(n) where n is the number of pixels in the image. We might process every pixel.
# Space: O(n) the size of the implicit call stack when calling dfs.
# ---------------------------------------------------------------------

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        old_color = image[sr][sc]
        
        if old_color != color:
            self.helper(image, sr, sc, old_color, color)
        
        return image
        
    def helper(self, image, i, j, old_color, new_color):
        
        if i < 0 or i > len(image) - 1:
            return
        
        if j < 0 or j > len(image[0]) - 1:
            return
        
        if image[i][j] != old_color:
            return
        else:
            image[i][j] = new_color
            
            self.helper(image, i, j - 1, old_color, new_color)            
            self.helper(image, i, j + 1, old_color, new_color)            
            self.helper(image, i - 1, j, old_color, new_color)            
            self.helper(image, i + 1, j, old_color, new_color)


# Second Solution from LeetCode
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image