class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        # Step 1: Generate all cell coordinates
        matrix = [[(r, c) for c in range(cols)] for r in range(rows)]

        # Step 2: Store distances in a list (instead of a dictionary)
        res = []
        for row in range(rows):
            for col in range(cols):
                dist = abs(rCenter - row) + abs(cCenter - col)  # Correct distance formula
                res.append(((row, col), dist))

        # Step 3: Sort by Manhattan distance
        res.sort(key=lambda x: x[1])  # Sort based on the second element (distance)

        # Step 4: Extract and return the sorted coordinates
        return [cell[0] for cell in res]
