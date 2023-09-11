#!/usr/bin/env python3

import curses


class button:

    def __init__(self, color, value: str):
        """
        Initialise a button. This button contains a value text which will be displayed within sharp brackets.
        A button is by default deactivated but can be active

        Parameters
        ----------
        color :
            The color scheme of the button. If the button is active the color scheme will be inverted.
        value : str
            The title of the button.

        """
        self.color = color
        self.value = value
        self.size = (1, len(value) + 2)  # size in Y and X direction
        self.active = False

    def attach_win(self, start_y: int, start_x: int):
        """
        When the final position of this object was calculated this function will create a window object which will contain the button.

        Parameters
        ----------
        start_y : int
            The Y coordinate where the window should start
        start_x : int
            The X coordinate where the window should start
        """
        self.window = curses.newwin(self.size[0], self.size[1], start_y, start_x)
        self.window.bkgd(self.color)
        self.deactivate()  # buttons are deactivated by default

    def activate(self):
        """
        Activate the button. This change still has to be redrawn by calling the draw() function.
        """
        curses.curs_set(0)
        self.window.attroff(curses.A_REVERSE)

    def deactivate(self):
        """
        Deactivate the button. This change still has to be redrawn by calling the draw() function.
        """
        curses.curs_set(1)
        self.window.attron(curses.A_REVERSE)

    def draw(self):
        """
        Draw the button or update the drawing of the button
        """
        self.window.insstr(0, 0, f"<{self.value}>")
        self.window.refresh()

    '''
    # TODO: I do not know wether the input() dummy function is needed or not but if it is needed: uncomment it
    def input(self, in_char: [str, int]) -> [str, int]:
        """
        Dummy function because a button takes no input but every object needs the input() method
        """
        return in_char
    '''
