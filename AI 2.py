import heapq
# Imports heapq module to implement a priority queue.
# It always selects the element with the lowest priority value.

# Goal state
goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)
# Defines the final arrangement of the puzzle.
# 0 represents the blank space.


# Calculate heuristic h(n)
def heuristic(state):
    # Defines a function to calculate misplaced tiles.
    h = 0
    # Initializes heuristic cost to zero.

    for i in range(9):
        # Loops through all 9 puzzle positions.

        if state[i] != 0 and state[i] != goal[i]:
            # Checks whether a tile is misplaced.
            # Ignores 0 because it represents blank space.

            h += 1
            # Increases heuristic value by 1.

    return h
    # Returns the total number of misplaced tiles.


# Generate next states
def get_neighbors(state):
    # Defines a function to generate possible next states.
    neighbors = []
    # Creates an empty list to store neighboring states.

    zero = state.index(0)
    # Finds the position of blank space (0).

    row = zero // 3
    # Calculates row number using floor division.

    col = zero % 3
    # Calculates column number using modulus.

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]
    # Defines four possible directions of movement.

    for dr, dc in moves:
        # Checks each possible movement.

        new_row = row + dr
        # Calculates the new row.

        new_col = col + dc
        # Calculates the new column.

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            # Checks whether the new position is inside the puzzle.

            new_zero = new_row * 3 + new_col
            # Converts row and column into a single index.

            new_state = list(state)
            # Converts tuple into a list so values can be changed.

            new_state[zero], new_state[new_zero] = (
                new_state[new_zero],
                new_state[zero]
            )
            # Swaps blank space with its neighboring tile.

            neighbors.append(tuple(new_state))
            # Converts the new list into a tuple and stores it.

    return neighbors
    # Returns all possible neighboring states.


# A* Algorithm
def a_star(start):
    # Defines the A* search function.
    # start represents the initial puzzle state.

    pq = []
    # Creates an empty priority queue.

    initial_g = 0
    # Actual cost from the initial state is zero.

    initial_h = heuristic(start)
    # Calculates misplaced tiles in the initial state.

    initial_f = initial_g + initial_h
    # Calculates total cost using f(n) = g(n) + h(n).

    print("INITIAL STATE")
    print("g =", initial_g)
    print("h =", initial_h)
    print("f = g + h =", initial_f)
    print()
    # Displays the initial state's cost values.

    heapq.heappush(
        pq,
        (initial_f, initial_g, start, [])
    )
    # Inserts initial state into priority queue.
    # Stores f, g, state and path.

    visited = set()
    # Creates an empty set to store visited states.

    while pq:
        # Continues searching while the queue is not empty.

        f, g, state, path = heapq.heappop(pq)
        # Removes the state having the lowest f-value.

        if state in visited:
            # Checks whether the state was already visited.
            continue
            # Skips an already visited state.

        visited.add(state)
        # Adds the current state to visited set.

        if state == goal:
            # Checks whether the goal state is reached.
            return path + [state]
            # Returns the complete solution path.

        for next_state in get_neighbors(state):
            # Generates and checks all neighboring states.

            if next_state not in visited:
                # Processes only unvisited states.

                new_g = g + 1
                # Increases actual cost by one move.

                new_h = heuristic(next_state)
                # Calculates misplaced tiles in next state.

                new_f = new_g + new_h
                # Calculates total estimated cost.

                print("Next State:", next_state)
                print("g =", new_g)
                print("h =", new_h)
                print("f = g + h =", new_f)
                print("--------------------")
                # Displays neighboring state and its costs.

                heapq.heappush(
                    pq,
                    (
                        new_f,
                        new_g,
                        next_state,
                        path + [state]
                    )
                )
                # Inserts the neighboring state into priority queue.
                # Also stores its previous path.

    return None
    # Returns None if no solution is found.


# Initial state
start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)
# Defines the starting puzzle arrangement.


# Solve the puzzle
solution = a_star(start)
# Calls A* algorithm and stores the solution path.


# Display solution
print("\nSOLUTION PATH")
print("================")
# Prints the solution heading.

for state in solution:
    # Loops through every state in the solution path.

    print(state[0], state[1], state[2])
    # Prints first row.

    print(state[3], state[4], state[5])
    # Prints second row.

    print(state[6], state[7], state[8])
    # Prints third row.

    print()
    # Prints an empty line between states.
