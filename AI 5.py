from collections import deque
# Imports deque, which is used to create an efficient queue.

# Grid
grid = [
    ['S', 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 'G']
]
# Creates a 4x4 grid.
# S = Start, G = Goal, 0 = Free cell, 1 = Obstacle.

# Start and goal positions
start = (0, 0)
goal = (3, 3)
# Defines the starting and destination coordinates.

# Queue
queue = deque([start])
# Creates a queue and inserts the starting position.

# Visited cells
visited = {start}
# Stores already visited positions to avoid repetition.

# Store parent of each cell
parent = {start: None}
# Stores the previous position of each cell.
# Start has no parent, so its parent is None.

# Four possible movements
directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]
# Defines four possible movement directions.


# BFS
while queue:
    # Runs while the queue contains elements.

    current = queue.popleft()
    # Removes and returns the first element from the queue.

    # Check whether goal is reached
    if current == goal:
        break
        # Stops searching when goal is found.

    # Check all four directions
    for dr, dc in directions:
        # dr = Change in row.
        # dc = Change in column.
        new_row = current[0] + dr
        # Calculates the new row position.

        new_col = current[1] + dc
        # Calculates the new column position.

        # Check whether position is inside grid
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            # Checks whether the new position is within grid boundaries.

            new_position = (new_row, new_col)
            # Creates a tuple containing new coordinates.

            # Check whether cell is free and not visited
            if grid[new_row][new_col] != 1 and new_position not in visited:
                # Checks that cell is not an obstacle
                # and has not already been visited.

                visited.add(new_position)
                # Marks the new position as visited.

                parent[new_position] = current
                # Stores the previous position (parent).

                queue.append(new_position)
                # Adds the new position to the queue.


# Construct the path
path = []
# Creates an empty list to store the final path.


if goal in parent:
    # Checks whether the goal has been reached.

    current = goal
    # Starts path reconstruction from the goal.

    while current is not None:
        # Continues until the starting position is reached.

        path.append(current)
        # Adds current position to the path.

        current = parent[current]
        # Moves backward to the parent position.

    path.reverse()
    # Reverses path to get Start-to-Goal order.

    print("Shortest Path:")
    # Displays heading.

    for position in path:
        # Iterates through every position in the path.

        print(position)
        # Prints each coordinate.

else:
    print("No path found")
    # Displays message if no valid path exists.
