from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    """
    A window class that creates a Tkinter GUI window with a canvas 
    for drawing shapes.

    Attributes:
        width (int): The width of the window.
        height (int): The height of the window.
        __root_widget (Tk): The root Tkinter window.
        canvas (Canvas): The canvas where shapes can be drawn.
        running (bool): A flag to indicate whether the window is running.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initializes the Window class with the given width and height,
        sets up the Tkinter root widget, and initializes the canvas.

        Args:
            width (int): The width of the window.
            height (int): The height of the window.
        """
        self.width = width
        self.height = height
        self.__root_widget = Tk()
        self.__root_widget.title("Maze Solver")
        self.__root_widget.geometry(f"{width}x{height}")
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(width=self.width, height=self.height, background='white')
        self.canvas.pack()
        self.running = False
    
    def redraw(self) -> None:
        """
        Redraws the window by processing pending GUI events. 
        Ensures that the interface remains responsive during updates.
        """
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self) -> None:
        """
        Enters a loop that keeps the window open until the user closes it.
        Continuously calls redraw() to update the window's state.
        """
        self.running = True

        while self.running:
            self.redraw()
    
    def close(self) -> None:
        """
        Gracefully closes the window by setting the running flag to False,
        allowing the main loop to exit.
        """
        self.running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        """
        Draws a line on the window's canvas using the Line class.

        Args:
            line (Line): The Line object containing the coordinates and logic for drawing.
            fill_color (str): The color used to draw the line.
        """
        line.draw(self.canvas, fill_color)
