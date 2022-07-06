from collections import deque

# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    paths = {}
    for s, d in ladders + snakes:
        paths[s] = d

    q = deque([(1, 0)])
    visited = set()
    while q:
        sq, rolls = q.popleft()
        if 100 == sq:
            return rolls

        visited.add(sq)
        for i in range(1, 7):
            next = sq + i
            if next in visited or next > 100:
                continue
            
            if next in paths:
                next = paths[next]
            q.append((next, rolls + 1))
    return -1


ladders = [[32, 62],
           [42, 68],
           [12, 98]]

snakes = [[95, 13],
          [97, 25],
          [93, 37],
          [79, 27],
          [75, 19],
          [49, 47],
          [67, 17]]

ladders2 = [[3, 54],
            [37, 100]]

snakes2 = [[56, 33]]

ladders3 = [[8, 37],
            [8, 100]]

snakes3 = [[88, 44]]

ladders4 = [[7, 98]]

snakes4 = [[99, 1]]


if __name__ == '__main__':
    print(quickestWayUp(ladders, snakes))
    print(quickestWayUp(ladders2, snakes2))  # 3
    print(quickestWayUp(ladders3, snakes3))  # 2
    print(quickestWayUp(ladders4, snakes4))  # 2
