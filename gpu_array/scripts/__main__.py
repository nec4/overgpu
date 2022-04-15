#! /usr/bin/env python

from overgpu.query import *
from overgpu.tui import *


def main():
    query = GPUQuery()
    tracker = Tracker(query)
    screen = curses_init()
    rows, cols = screen.getmaxyx()
    front = FrontEnd(tracker, rows, cols)
    ch = None
    front.refresh(screen)
    front.run()
    while ch != ord("q"):
        ch = screen.getch()
        if curses.is_term_resized(rows, cols):
            curses.endwin()
            screen = curses_init()
            rows, cols = screen.getmaxyx()
            curses.resizeterm(rows, cols)
            front.resize(rows, cols)
            screen.refresh()
            continue
        if ch == ord("p"):
            front._swap_view()
            front.refresh(screen)
            continue
        else:
            front.refresh(screen)
    front.stop()
    curses.endwin()


if __name__ == "__main__":
    main()