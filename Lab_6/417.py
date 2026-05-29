class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col, can_reach):
            can_reach.add((row, col))

            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy

                if (0 <= next_row < rows) and (0 <= next_col < cols):
                    if (next_row, next_col) not in can_reach and heights[next_row][next_col] >= heights[row][col]:
                        dfs(next_row, next_col, can_reach)
        pacific = set()
        atlantic = set()

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)
        
        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)
        
        return list(pacific & atlantic)
    