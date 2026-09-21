from line import Line, Point
from window import Window

class Cell:
    """
    Represents a cell in a grid-based maze. Each cell has four walls that may 
    or may not be present, and the cell's status as visited is tracked.

    Attributes:
        _x1 (int): X-coordinate of the top-left corner.
        _y1 (int): Y-coordinate of the top-left corner.
        _x2 (int): X-coordinate of the bottom-right corner.
        _y2 (int): Y-coordinate of the bottom-right corner.
        _win (Window): The window object where the cell will be drawn.
        has_left_wall (bool): Indicates whether the cell has a left wall.
        has_right_wall (bool): Indicates whether the cell has a right wall.
        has_top_wall (bool): Indicates whether the cell has a top wall.
        has_bottom_wall (bool): Indicates whether the cell has a bottom wall.
        visited (bool): Tracks whether the cell has been visited.
    """
    
    def __init__(
        self,
        x1: int = 0,
        y1: int = 0,
        x2: int = 0,
        y2: int = 0,
        window: Window = None
    ) -> None:
        """
        Initializes the cell with the given coordinates and window.

        Args:
            x1 (int): X-coordinate of the top-left corner.
            y1 (int): Y-coordinate of the top-left corner.
            x2 (int): X-coordinate of the bottom-right corner.
            y2 (int): Y-coordinate of the bottom-right corner.
            window (Window): The window where the cell will be drawn.
        """
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = window

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.visited = False
        
    def draw(self) -> None:
        """
        Draws the cell's walls on the window's canvas. If a wall is present, 
        it is drawn in black; if not, it is drawn in white (indicating a removed wall).
        """
        
        top_left_vertex = Point(self._x1, self._y1)
        top_right_vertex = Point(self._x2, self._y1)
        bottom_left_vertex = Point(self._x1, self._y2)
        bottom_right_vertex = Point(self._x2, self._y2)

        left_wall = Line(top_left_vertex, bottom_left_vertex)
        right_wall = Line(top_right_vertex, bottom_right_vertex)
        top_wall = Line(top_left_vertex, top_right_vertex)
        bottom_wall = Line(bottom_left_vertex, bottom_right_vertex)
        
        if self._win is not None:
            if self.has_left_wall:
                left_wall.draw(self._win.canvas, 'black')
            else:
                left_wall.draw(self._win.canvas, 'white')

            if self.has_right_wall:
                right_wall.draw(self._win.canvas, 'black')
            else:
                right_wall.draw(self._win.canvas, 'white')

            if self.has_top_wall:
                top_wall.draw(self._win.canvas, 'black')
            else:
                top_wall.draw(self._win.canvas, 'white')

            if self.has_bottom_wall:
                bottom_wall.draw(self._win.canvas, 'black')
            else:
                bottom_wall.draw(self._win.canvas, 'white')

    def draw_move(self, to_cell: 'Cell', undo: bool = False) -> None:
        """
        Draws a move from the current cell to the target cell. The line is 
        drawn in red when making the move, or gray if the move is being undone.

        Args:
            to_cell (Cell): The target cell to move to.
            undo (bool): If True, draws the move in gray (undo); otherwise, in red.
        """
        
        if self._win is None:
            return

        # Calculate the center points of both cells to draw a move between them.
        self_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_cell_center = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)

        center_to_center = Line(self_center, to_cell_center)

        if not undo:
            center_to_center.draw(self._win.canvas, 'red')
        else:
            center_to_center.draw(self._win.canvas, 'gray')
