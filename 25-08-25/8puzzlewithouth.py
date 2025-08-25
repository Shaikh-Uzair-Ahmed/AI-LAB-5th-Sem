#without heuristic 
from collections import deque

# Goal state for the 8 puzzle
goal_state = '123456780'  # Using '0' as the empty tile

# Moves: U, D, L, R (Up, Down, Left, Right)
moves = {
    'U': -3,
    'D': 3,
    'L': -1,
    'R': 1
}

# Valid moves for each index to prevent wrapping around rows/columns
invalid_moves = {
    0: ['U', 'L'], 1: ['U'], 2: ['U', 'R'],
    3: ['L'],        5: ['R'],
    6: ['D', 'L'], 7: ['D'], 8: ['D', 'R']
}

# Function to generate new puzzle state after moving the blank
def move_tile(state, direction):
    index = state.index('0')
    if direction in invalid_moves.get(index, []):
        return None

    new_index = index + moves[direction]
    if new_index < 0 or new_index >= 9:
        return None

    state_list = list(state)
    # Swap 0 with the target tile
    state_list[index], state_list[new_index] = state_list[new_index], state_list[index]
    return ''.join(state_list)

# BFS Algorithm
def bfs(start_state):
    visited = set()
    queue = deque([(start_state, [])])  # Each element is (state, path)

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path

        visited.add(current_state)

        for direction in moves:
            new_state = move_tile(current_state, direction)
            if new_state and new_state not in visited:
                queue.append((new_state, path + [direction]))

    return None  # No solution found

# Input initial state as a string (e.g., '123456780' where 0 is the blank)
start = input("Enter start state (e.g., 724506831): ")

if len(start) == 9 and set(start) == set('012345678'):
    result = bfs(start)
    if result is not None:
        print("Solution found!")
        print("Moves:", ' '.join(result))
        print("Number of moves:", len(result))
        print("1BM23CS307 Uzair")
    else:
        print("No solution exists for the given start state.")
else:
    print("Invalid input! Please enter a 9-digit string using digits 0-8 without repetition.")
