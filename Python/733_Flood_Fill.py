# 1 Possible Solutions
# 1. DFS

# Time: O(M*N), Space: O(M*N)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # If Image is empty or the color provided is already that color
        if not image or image[sr][sc] == newColor:
            return image

        self._floodFill(image, sr, sc, image[sr][sc], newColor):
        return image
    
    def _floodFill(self, image, sr, sc, initialColor, newColor):
        # Check for bounds
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != initialColor:
            return
        
        image[sr][sc] = newColor

        self._floodFill(image, sr + 1, sc, initialColor, newColor) # down
        self._floodFill(image, sr - 1, sc, initialColor, newColor) # up
        self._floodFill(image, sr, sc + 1, initialColor, newColor) # right
        self._floodFill(image, sr, sc - 1, initialColor, newColor) # left
        