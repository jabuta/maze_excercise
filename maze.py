from time import sleep
from cell import Cell
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1
        y1 = self._y1

        cell_x1 = x1 + i * self._cell_size_x
        cell_y1 = y1 + j * self._cell_size_y
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)

        self._animate()

    def _animate(self,time=0.01):
        if self._win is None:
            return
        self._win.redraw()
        sleep(time)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            possible = []
#left
            if i > 0 and not self._cells[i - 1][j].visited:
                possible.append([i - 1, j])
#right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                possible.append([i + 1, j])            
#down
            if j > 0 and not self._cells[i][j - 1].visited:
                possible.append([i, j - 1])
#up
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                possible.append([i, j + 1])
            if not possible:
                self._draw_cell(i, j)
                return
            next_cell = random.choice(possible)
            
            if next_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_right_wall = False
            elif next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_left_wall = False
            elif next_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_bottom_wall = False
            elif next_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_top_wall = False

            self._break_walls_r(next_cell[0], next_cell[1])
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
#right
        if (i < self._num_cols - 1 and
            not self._cells[i+1][j].visited and
            not self._cells[i][j].has_right_wall):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j],undo=True)
#left
        if (i > 0 and
            not self._cells[i-1][j].visited and
            not self._cells[i][j].has_left_wall):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j],undo=True)
#down
        if (j < self._num_rows - 1 and
            not self._cells[i][j+1].visited and
            not self._cells[i][j].has_bottom_wall):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1],undo=True)
#up
        if (j > 0 and
            not self._cells[i][j-1].visited and
            not self._cells[i][j].has_top_wall):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1],undo=True)
        
        return False
 # working on bfs   
    def solve_bfs(self):
        self._animate()
        self._cells[i][j].visited = True
        while 
        
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
    def breadth_first_search(self, v):
        visited = []
        to_visit = [start]
        path = {start: None}
        while to_visit:
            current_vertex = to_visit.pop(0)
            visited.append(current_vertex)
            if current_vertex == end:
                path_list = []
                while current_vertex is not None:
                    path_list.append(current_vertex)
                    current_vertex = path[current_vertex]
                path_list.reverse()
                return path_list

            sorted_neighbors = sorted(self.graph[current_vertex])
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
                    path[neighbor] = current_vertex
        return None
