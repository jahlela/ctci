

def get_path_bool(maze):
    if not maze:
        return None

    path = []
    failed = set()

    # If you can reach the end of the maze, return the path
    if get_path(maze, len(maze) - 1, len(maze[0] - 1, path, failed)):
        return path

    return None


def get_path(maze, row, col, failed):
    if col < 0 or row < 0 or !maze[row][col]:
        return False

    new_point = (row, col)

    if new_point in failed:
        return False

    is_at_origin = (row == 0) and (col == 0)

    can_go_up = get_path(maze, row-1, col, path, failed)
    can_go_left = get_path(maze, row, col-1, path, failed)
                
    if is_at_origin or can_go_up or can_go_left:
        path.add(new_point)
        return True

    failed.add(new_point)
    return False

                

