#!/usr/bin/python3
import curses
import time

def main(stdscr):
    # 初始化颜色
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    # 隐藏光标
    curses.curs_set(0)

    # 窗口设置
    height, width = stdscr.getmaxyx()
    textpad_height, textpad_width = 3, 40
    textpad_win = curses.newwin(textpad_height, textpad_width, height//2 - 2, width//2 - textpad_width//2)
    textpad_win.box()

    button_win = curses.newwin(3, 20, height//2 + 2, width//2 - 10)
    button_win.box()
    button_win.addstr(1, 1, "Press Enter", curses.color_pair(1))

    stdscr.refresh()
    textpad_win.refresh()
    button_win.refresh()

    # 等待用户按下回车键
    while True:
        key = stdscr.getch()
        if key == curses.KEY_ENTER or key in [10, 13]:
            textpad_win.addstr(1, 1, "Button Clicked!", curses.color_pair(2))
            time.sleep(3)  # 暂停3秒
            textpad_win.refresh()
            break

if __name__ == "__main__":
    curses.wrapper(main)
