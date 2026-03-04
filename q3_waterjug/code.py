from collections import deque

# BFS function
def water_jug_bfs():

    visited = set()
    queue = deque([(0, 0)])   # initial state

    while queue:

        state = queue.popleft()
        x, y = state

        if state in visited:
            continue

        visited.add(state)

        print("Current State:", state)

        # Goal condition
        if x == 2:
            print("Goal reached with state:", state)
            return

        # Possible next states
        next_states = [
            (4, y),   # fill 4L jug
            (x, 3),   # fill 3L jug
            (0, y),   # empty 4L jug
            (x, 0),   # empty 3L jug
            (max(0, x - (3 - y)), min(3, y + x)),  # pour 4L -> 3L
            (min(4, x + y), max(0, y - (4 - x)))   # pour 3L -> 4L
        ]

        for new_state in next_states:
            if new_state not in visited:
                queue.append(new_state)

# Run program
water_jug_bfs()
