"""
The curses module is used to handle user keypresses,
allowing them to move the snake
"""

import curses
import os
import time


def main():

    stdscr = curses.initscr()
    curses.start_color()

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # # add text top screen
    curses.noecho()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.addstr(10, 10, "Sree is here!", curses.color_pair(1))
    stdscr.refresh()
    curses.echo()
    time.sleep(1)
    k = stdscr.getch()


if __name__ == "__main__":
    os.environ.setdefault("TERM", "xterm")
    os.environ.setdefault("TERMINFO", "/etc/terminfo")
    main()
