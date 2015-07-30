import curses

################################################################################
################################################################################
##  mainUI class
## represents the curses ui that the user interacts with
################################################################################
################################################################################
class mainUI(object):
    #constructor
    def __init__(self, stdscr, calGen):
        curses.curs_set(False)
        self.scr = stdscr
        self.scr.keypad(True)
        self.menuItems = ["Generate Calendar", "My Teams", "Sync to Google", "Exit"]
        self.selectedItem = 0
        self.calGen = calGen

    #start the main ui oop
    def start(self):
        go = True
        while go:
            self.drawMenu()
            key = self.scr.getkey()
            self.updateSelectedItem(key)

            if self.isSelectionKey(key):
                menuSelection = self.menuItems[self.selectedItem]
                if menuSelection == "Exit":
                    go = False
                elif menuSelection == "Generate Calendar":
                    self.generateCalendar()
                elif menuSelection == "My Teams":
                    self.myTeams()
                elif menuSelection == "Sync to Google":
                    self.syncToGoogle()



    #####################
    # Menu helper functions
    #####################

    #updates the selected item based on what key was pressed
    def updateSelectedItem(self, key):
        amountOfItems = len(self.menuItems)
        curSel = self.selectedItem
        if key == "KEY_DOWN":
            if curSel < amountOfItems - 1:
                curSel = curSel + 1
            elif curSel == amountOfItems - 1:
                curSel = 0

        elif key == "KEY_UP":
            if curSel > 0:
                curSel = curSel -1
            elif curSel == 0:
                curSel = amountOfItems - 1

        #apply the change
        self.selectedItem = curSel

    #Checks if the given key is a valid selection key
    def isSelectionKey(self, key):
        return (key == "\n" or key == "KEY_RIGHT")

    #clears the screen and applies standard menu decorations
    def clearAndDecorate(self):
        self.scr.clear()
        size = self.scr.getmaxyx()

        for i in range(0,size[0]):
            self.scr.addstr(i,0,"......")

    #Draws a standard menu
    def drawMenu(self):
        self.clearAndDecorate()
        for i in range(0, len(self.menuItems)):
            prefix = "----->\t"
            if i == self.selectedItem:
                prefix = "------>\t"

            self.scr.addstr(i+2, 0, prefix+ self.menuItems[i])

    #####################
    # Selection screen functions
    #####################

    #main function to let a user select an item out of a list
    def getUserSelection(self, items):
        res = None

        curses.echo()
        curses.nocbreak()
        go = True
        msg = ""
        while go:
            self.drawItems(items, msg)
            inp = self.scr.getstr()

            try:
                selection = int(inp)

                #prevent python from selecting items from the end of the list
                if selection < 1:
                    raise IndexError

                #check if an existing number was selected
                #(error will be raised if this is not the case)
                res = items[selection - 1]
                go = False
            except ValueError as ve:
                msg = "(Invalid input, try again)"
            except IndexError as ie:
                msg = "(Invalid selection, try again)"

        curses.noecho()
        curses.cbreak()

        return res

    def drawItems(self, items, msg=""):
        dimensions = self.scr.getmaxyx()
        self.scr.clear()
        for i in range(0,len(items)):
            self.scr.addstr(i,0,str(i + 1) + '. ' + items[i])

        self.scr.addstr(dimensions[0]-2,0, "Enter your selection: " + msg)
        self.scr.move(dimensions[0] - 1, 0)

    #####################
    # Menu actions
    #####################
    def generateCalendar(self):
        #select federation
        fedList = self.calGen.getFederations()
        federation = self.getUserSelection(fedList)

        #select league
        leagueList = self.calGen.getLeagues(federation)
        league = self.getUserSelection(leagueList)

    def myTeams(self):
        self.scr.clear()
        self.scr.addstr(0,0,"Team view not available yet")
        self.scr.getch()

    def syncToGoogle(self):
        self.scr.clear()
        self.scr.addstr(0,0,"Google syncing not available yet")
        self.scr.getch()
