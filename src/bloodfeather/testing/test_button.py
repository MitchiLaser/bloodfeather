#!/usr/bin/env python3
# -*- encoding: utf8 -*-

import curses
import os
import sys

# make sure the button file can be imported
path = os.path.abspath("./../form")
sys.path.append(path)
# prevent the auto formatter from moving this import to the front
if True:
    import button


def main(stdscr: curses.window):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    COLORS = curses.color_pair(1)

    stdscr.refresh()
    ok_button = button.button(COLORS, "OK")
    heigth, length = stdscr.getmaxyx()
    ok_button.attach_win(heigth // 2, length // 2)
    ok_button.activate()
    ok_button.draw()

    _ = stdscr.get_wch()


curses.wrapper(main)
