class Shape:
    """Drawing primitives for a Tkinter canvas."""

    def __init__(self, canvas):
        self.canvas = canvas

    def draw_oval(self, x, y, diameter, color):
        """Draw a filled oval centered at (x, y)."""
        self.canvas.create_oval(
            x - diameter, y - diameter,
            x + diameter, y + diameter,
            fill=color)

    def draw_square(self, x, y, side_len, color):
        """Draw a filled square centered at (x, y)."""
        half = side_len / 2
        self.canvas.create_rectangle(
            x - half, y - half,
            x + half, y + half,
            fill=color)
