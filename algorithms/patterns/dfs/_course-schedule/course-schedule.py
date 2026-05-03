# https://leetcode.com/problems/course-schedule/

# %%

# Classical DFS three-colour cycle detection.
#
# Model: each prerequisite pair [a, b] = "b must be taken before a" becomes a
# directed edge b -> a. The question "can all courses be finished?" is exactly
# "is this directed graph acyclic?" → "does a topological sort exist?".
#
# Three colours track each node's state during DFS:
#   WHITE = unvisited (not yet touched)
#   GREY  = currently on the DFS recursion stack (being explored)
#   BLACK = fully explored — proven to lie on no cycle
#
# A cycle exists iff DFS encounters a GREY neighbour, i.e. a back edge into a
# node that is still being explored on the current path.
#
# Time:  O(V + E) — every node and edge is touched at most once.
# Space: O(V + E) — adjacency list + colour array + recursion stack.
#        Recursion depth can reach V (up to 2000 for this problem) which is
#        above Python's default recursion limit (1000) — bump it for LeetCode
#        or use Kahn's BFS / iterative DFS for production.


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph: list[list[int]] = [[] for _ in range(num_courses)]
    for a, b in prerequisites:
        graph[b].append(a)  # edge "prereq -> dependent"

    WHITE, GREY, BLACK = 0, 1, 2
    color = [WHITE] * num_courses

    def has_cycle(node: int) -> bool:
        if color[node] == BLACK:
            return False  # already proven safe
        if color[node] == GREY:
            return True  # back edge → cycle
        color[node] = GREY
        for nxt in graph[node]:
            if has_cycle(nxt):
                return True
        color[node] = BLACK
        return False

    for i in range(num_courses):
        if has_cycle(i):
            return False
    return True


# Examples from the problem statement
assert can_finish(2, [[1, 0]]) is True
assert can_finish(2, [[1, 0], [0, 1]]) is False

# Trivial cases
assert can_finish(1, []) is True
assert can_finish(5, []) is True

# A chain is a DAG → True
assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) is True

# A 3-cycle hidden among unrelated edges → False
assert can_finish(3, [[0, 1], [1, 2], [2, 0]]) is False

# Two disconnected components, both acyclic → True
assert can_finish(5, [[1, 0], [2, 1], [4, 3]]) is True

# Self-loop is a cycle of length 1 → False
assert can_finish(2, [[0, 0]]) is False
