import collections


def is_next_available(current_letter: str, next_letter: str) -> bool:
    if next_letter == 'E':
        return current_letter == 'z'

    if current_letter == 'S':
        return next_letter == 'a'

    distance = ord(next_letter) - ord(current_letter)

    return distance <= 1


surrounding_area = [[x for x in line.strip()] for line in open("input.txt").readlines()]


def bfs(grid, start, goal):
    queue = collections.deque()
    seen = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == start:
                queue.append([(i, j)])
                seen.add((i, j))

    width = len(grid)
    height = len(grid[0])

    while queue:
        path = queue.popleft()
        x, y = path[-1]

        if grid[x][y] == goal:
            return path

        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (0 <= x2 < width) and (0 <= y2 < height) and (x2, y2) not in seen \
                    and is_next_available(grid[x][y], grid[x2][y2]):
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


path_part_one = bfs(surrounding_area, 'S', 'E')
path_part_two = bfs(surrounding_area, 'a', 'E')

print(len(path_part_one) - 1)
print(len(path_part_two) - 1)
