import time
from maze import Maze
from collections import deque

def solve_maze(maze):
    stack = deque()
    
    # Posição inicial do jogador
    init_pos = maze.get_init_pos_player()
    
    # Localização inicial na pilha
    stack.append(init_pos)
    
    while stack:
        current_pos = stack.pop()
        
        if maze.find_prize(current_pos):
            print("Caminho foi encontrado!")
            return True
        
        if maze.is_free(current_pos):
            maze.mov_player(current_pos)
            
            # Examina se as casas adjacentes estão livres
            x, y = current_pos
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < maze.M.shape[0] and 0 <= new_y < maze.M.shape[1]:
                    if maze.is_free((new_x, new_y)):
                        stack.append((new_x, new_y))
    
    print("Caminho não foi encontrado.")
    return False

maze_csv_path = "labirinto1.txt"  

maze = Maze()
maze.load_from_csv(maze_csv_path)

maze.run()
maze.init_player()

solve_maze(maze)

time.sleep(10)