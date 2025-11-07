class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        # count = 0
        # length = len(grid)

        # for i in range(length):
        #     for j in range(length):
        #         for k in range(length):
        #             if grid[i][k] != grid[k][j]:
        #                 break
        #             if k == length-1:
        #                 count += 1

        # return count

        count = 0
        row_count = {}

        for row in grid:
            key = tuple(row)
            row_count[key] = row_count.get(key, 0) + 1

        for i in range(len(grid)):
            col = tuple(grid[j][i] for j in range(len(grid)))
            if col in row_count:
                count += row_count[col]

        return count
