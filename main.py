import curses

def isSelectionKey(key):
    return (key == "\n" or key == "KEY_RIGHT")




#Clears the screen and adds the standard menu decorations
def clearAndDecorate(scr):
    scr.clear()
    size = scr.getmaxyx()

    for i in range(0,size[0]):
        scr.addstr(i,0,"......")




#Draws a standard menu, based on the given parameters
def drawMenu(scr, menuItems, selectedItem):
    clearAndDecorate(scr)
    for i in range(0, len(menuItems)):
        prefix = "----->\t"
        if i == selectedItem:
            prefix = "------>\t"

        scr.addstr(i+2, 0, prefix+menuItems[i])




#Returns the new selected item based on previous current selection,
#the amount of menu items available and the key that was pressed
def updateSelectedItem(currentSelection, amountOfItems, key):
    #Don't change position on invalid key
    res = currentSelection

    if key == "KEY_DOWN":
        if currentSelection < amountOfItems - 1:
            res = currentSelection + 1
        elif currentSelection == amountOfItems - 1:
            res = 0

    elif key == "KEY_UP":
        if currentSelection > 0:
            res = currentSelection -1
        elif currentSelection == 0:
            res = amountOfItems - 1

    return res





def syncScreen(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0,"Nothing here yet")
    stdscr.getch()




def myTeamsScreen(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0,"Nothing here yet")
    stdscr.getch()




def generateScreen(stdscr):

    selectedItem = 0
    go = True
    menuOptions = ["VVB", "volley Vlaams-Brabant", "AVF","Back to Main Menu"]
    while go:

        drawMenu(stdscr, menuOptions ,selectedItem)
        key = stdscr.getkey()
        selectedItem = updateSelectedItem(selectedItem, len(menuOptions), key)

        if isSelectionKey(key):
            if selectedItem == 3:
                go = False




def main(stdscr):

    selectedItem = 0
    go = True
    menuOptions = ["Generate Calendar", "My Teams", "Sync to Google","Exit"]
    while go:

        drawMenu(stdscr, menuOptions ,selectedItem)
        key = stdscr.getkey()
        selectedItem = updateSelectedItem(selectedItem, len(menuOptions), key)

        if isSelectionKey(key):
            if selectedItem == 0:
                generateScreen(stdscr)
            elif selectedItem == 1:
                myTeamsScreen(stdscr)
            elif selectedItem == 2:
                syncScreen(stdscr)
            elif selectedItem == 3:
                go = False




if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.curs_set(False)

    main(stdscr)

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    
