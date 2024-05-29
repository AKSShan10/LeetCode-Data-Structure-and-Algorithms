class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        s_p = image[sr][sc]
        self.dfs(image, sr, sc, color, s_p)
        return image

    def dfs(self,image, sr, sc, color, s_p):
        if sr <0 or sr > len(image)-1 or sc > len(image[0])-1 or sc<0 or image [sr][sc] == color or image[sr][sc] != s_p:
            return

        image[sr][sc] = color
        self.dfs(image, sr+1, sc, color, s_p)
        self.dfs(image, sr-1, sc, color, s_p)
        self.dfs(image, sr, sc+1, color, s_p)
        self.dfs(image, sr, sc-1, color, s_p)