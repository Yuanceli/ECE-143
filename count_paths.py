def count_paths(m,n,blocks):
    '''
    m*n grid
    # is block
    . is pass
    '''
    assert isinstance(m, int) and isinstance(n, int)
    assert m > 0 and n > 0
    assert isinstance(blocks, list)
    maze = []
    for i in range(m):
        maze.append([])
        for j in range(n):
            maze[i].append(0)
    maze[0][0] = 1
    for b in blocks:
        assert isinstance(b, tuple)
        assert (isinstance(p, int) for p in b)
        assert b != (0, 0)
        maze[b[0]][b[1]] = -1
    
    for i in range(m):
        for j in range(n):
            if (maze[i][j] == -1):
                continue

            if (maze[i - 1][j] > 0):
                maze[i][j] = (maze[i][j] + maze[i - 1][j])
            if (maze[i][j - 1] > 0):
                maze[i][j] = (maze[i][j] + maze[i][j - 1])
    print(maze)
    return maze[m - 1][n - 1]
