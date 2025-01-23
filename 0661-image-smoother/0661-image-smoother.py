class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])

        res = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                total = 0
                count = 0
                for i in range(r-1, r + 2):
                    for j in range(c-1, c+2):

                        if i < 0 or i >= rows or j < 0 or j >= cols:
                            continue
                        total += img[i][j]
                        count += 1
                
                avg_ = total // count
                res[r][c] = avg_

        return res