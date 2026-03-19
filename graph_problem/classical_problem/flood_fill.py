import sys
# Flood fill is a classic algorithm used to determine and alter the area connected to a given node in a multi-dimensional array
# Increase recursion depth for large grids (e.g., 1000x1000)
sys.setrecursionlimit(1000000)

def flood_fill(grid, r, c, new_color):
    rows = len(grid)
    cols = len(grid[0])
    old_color = grid[r][c]
    
    # Base Case: If the starting pixel is already the new color, do nothing
    if old_color == new_color:
        return grid

    def dfs(curr_r, curr_c):
        # 1. Check Boundaries: Are we still inside the grid?
        if curr_r < 0 or curr_r >= rows or curr_c < 0 or curr_c >= cols:
            return
        
        # 2. Check Color: Is this pixel the color we want to change?
        if grid[curr_r][curr_c] != old_color:
            return

        # 3. Fill: Change the color
        grid[curr_r][curr_c] = new_color

        # 4. Recurse: Visit neighbors (Up, Down, Left, Right)
        dfs(curr_r + 1, curr_c) # Down
        dfs(curr_r - 1, curr_c) # Up
        dfs(curr_r, curr_c + 1) # Right
        dfs(curr_r, curr_c - 1) # Left

    dfs(r, c)
    return grid

# --- Example Usage ---
example_grid = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

# Start at row 1, col 1 (the center) and fill with color '2'
result = flood_fill(example_grid, 1, 1, 2)

for row in result:
    print(row)