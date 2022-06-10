"""
The curses module is used to handle user keypresses,
allowing them to move the snake
"""

import curses
import os
import time


def main(stdscr):

    print("Executing main...")
    time.sleep(10)

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # add text top screen
    stdscr.addstr(0, 0, "Sree is here!", curses.color_pair(1))

    k = stdscr.getch()


if __name__ == "__main__":
    os.environ.setdefault("TERM", "linux")
    os.environ.setdefault("TERMINFO", "/etc/terminfo")
    curses.wrapper(main)
