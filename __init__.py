import curses
import ui
import domain as dom

def main(stdscr):
    calGen = dom.calendarGenerator()
    mainui = ui.mainUI(stdscr, calGen)

    mainui.start()

if __name__ == '__main__':
    curses.wrapper(main)
