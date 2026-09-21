import random
from time import sleep

from cell import Cell
from window import Window


class Maze():
    def __init__(
        self,
        x1: int,
        y1: int,
        num_cols: int,
        num_rows: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window = None,
        seed: int = None
    ) -> None:
        
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self) -> None:
        self._cells = [[Cell(window=self._win) for _ in range(self.num_rows)] for _ in range(self.num_cols)]

        for i, row in enumerate(self._cells):
            for j, cell in enumerate(row):
                self._draw_cell(i, j)
        return self._cells
    
    def _draw_cell(self, i: int, j: int) -> None:
        cell = self._cells[i][j]
        cell._x1 = self._x1 + i * self.cell_size_x
        cell._y1 = self._y1 + j * self.cell_size_y
        cell._x2 = self._x1 + (i + 1) * self.cell_size_x
        cell._y2 = self._y1 + (j + 1) * self.cell_size_y

        cell.draw()
        self._animate()
        
    def _animate(self) -> None:
        if self._win:
            self._win.redraw()
            sleep(.025)

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i: int, j: int) -> None:
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            right = (i + 1, j)
            left = (i - 1, j)
            top = (i, j - 1)
            bottom = (i, j + 1)

            directions = (right, left, top, bottom)

            for direction in directions:
                d_i, d_j = direction

                if d_i < 0 or d_j < 0:
                    continue
                if d_i >= self.num_cols or d_j >= self.num_rows:
                    continue
                
                if self._cells[d_i][d_j].visited == False:
                        to_visit.append(direction)

            if len(to_visit) == 0:
                return
            
            else:
                next_i, next_j = random.choice(to_visit)

                direction = (next_i, next_j)
                cell = self._cells[i][j]

                if  direction == right:

                    cell.has_right_wall = False
                    self._cells[next_i][next_j].has_left_wall = False

                elif direction == left:

                    cell.has_left_wall = False
                    self._cells[next_i][next_j].has_right_wall = False

                elif direction == top:

                    cell.has_top_wall = False
                    self._cells[next_i][next_j].has_bottom_wall = False

                else:
                    cell.has_bottom_wall = False
                    self._cells[next_i][next_j].has_top_wall = False
                    
                self._draw_cell(i, j)

                self._break_walls_r(next_i, next_j)
    
    def _reset_cells_visited(self) -> None:
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self) -> bool:
        return self._solve_r(0, 0)
    
    def _solve_r(self, i: int, j: int) -> bool:
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        if current == self._cells[-1][-1]:
            return True
        
        right = (i + 1, j)
        left = (i - 1, j)
        top = (i, j - 1)
        bottom = (i, j + 1)
        
        directions = [right, left, top, bottom]

        for direction in directions:
            
            d_i, d_j = direction

            if d_i < 0 or d_j < 0:
                    continue
            if d_i >= self.num_cols or d_j >= self.num_rows:
                    continue

            
            if self._cells[d_i][d_j] and self._cells[d_i][d_j].visited == False:

                if direction == right:
                    if not self._wall_check(i, j, 'right'):
                        current.draw_move(self._cells[d_i][d_j])
                        if self._solve_r(d_i, d_j):
                            return True
                        else:
                            current.draw_move(self._cells[d_i][d_j], undo=True)
                elif direction == left:
                    if not self._wall_check(i, j, 'left'):
                        current.draw_move(self._cells[d_i][d_j])
                        if self._solve_r(d_i, d_j):
                            return True
                        else:
                            current.draw_move(self._cells[d_i][d_j], undo=True)
                elif direction == top:
                    if not self._wall_check(i, j, 'top'):
                        current.draw_move(self._cells[d_i][d_j])
                        if self._solve_r(d_i, d_j):
                            return True
                        else:
                            current.draw_move(self._cells[d_i][d_j], undo=True)
                elif direction == bottom:
                    if not self._wall_check(i, j, 'bottom'):
                        current.draw_move(self._cells[d_i][d_j])
                        if self._solve_r(d_i, d_j):
                            return True
                        else:
                            current.draw_move(self._cells[d_i][d_j], undo=True)
                else:
                    return False

        return False
                
    def _wall_check(self, i: int, j: int, direction: str) -> bool:
        cell = self._cells[i][j]
        if direction == 'right':
            if cell.has_right_wall:
                return True
            else:
                return False
        if direction == 'left':
            if cell.has_left_wall:
                return True
            else:
                return False
        
        if direction == 'top':
            if cell.has_top_wall:
                return True
            else:
                return False
        
        if direction == 'bottom':
            if cell.has_bottom_wall:
                return True
            else:
                return False