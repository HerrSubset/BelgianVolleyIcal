## This file contains all the scripts used to download information from the
## web and transform it to usable python data objects. These scripts are mainly
## used by the federation classes in the file domain.py

import datetime as DT
import domain as DOM
import requests
from bs4 import BeautifulSoup

def VVBLoadScript():
    leagues = []

    r = requests.post("http://www.volleyvvb.be/competitie-wedstrijden", data={"Reeks": "%", "Stamnummer": "%", "Week":"0"})

    html = r.text
    bs = BeautifulSoup(html)

    #find the correct starting element
    form = bs.find("form", method="post")
    table = form.find("table", cellpadding="1")
    tr = table.find("tr")

    #loop through all the rows
    currentKey = None
    go = True
    currentLeague = None
    while go:
        if startsNewDivision(tr):
            currentLeague = DOM.League(tr.td.text[12:])
            leagues.append(currentLeague)

        if containsGame(tr):
            currentLeague.addGame(createNewGame(tr))

        if tr.next_sibling == None:
            go = False
        else:
            tr = tr.next_sibling

    return leagues



#take data from given row to create a game object
def createNewGame(row):
    td = row.td
    homeTeam = None
    awayTeam = None
    location = None
    date = None

    td = td.next_sibling.next_sibling
    day = td.span.text
    #build time array
    ta = [int(day[6:]),int(day[3:5]),int(day[0:2])]

    td = td.next_sibling
    time = td.span.text
    ta.append(int(time[0:2]))    #append hour
    ta.append(int(time[3:]))   #append minutes

    #create date object
    date = DT.datetime(ta[0],ta[1],ta[2],ta[3],ta[4])

    td = td.next_sibling
    homeTeam = td.text
    homeTeam = cutTeamLetter(homeTeam)

    td = td.next_sibling
    awayTeam = td.text
    awayTeam = cutTeamLetter(awayTeam)

    td = td.next_sibling
    location = td.text

    return DOM.Game(homeTeam.lower(), awayTeam.lower(), date, location)


def cutTeamLetter(team):
    res = team
    if res[-2] == " ":
        res = res[0:-2]
    return res


#check if the given row contains a game
def containsGame(row):
    td = row.find("td")
    return classEquals(td, "wedstrijd")


#checks if the given tr starts a new division by checking if the tr has a td
#with the "vvb_titel2" class
def startsNewDivision(row):
    td = row.find("td")
    return classEquals(td, "vvb_titel2")


#check if the class of an element equals to the given classname
def classEquals(element, className):
    res = False

    try:
        if element.attrs["class"][0] == className:
            res = True
    except KeyError as err:     #handle error if element has no class
        res = False

    return res




#####################################################
# Test loading scripts
#####################################################
def testLS():
    res = []
    #first test league
    league1 = DOM.League("Liga A")

    date = DT.datetime(2015, 9, 15, 20, 30)
    game = DOM.Game("vvbteam1", "vvbteam2", date, "sportshall")
    league1.addGame(game)

    date = DT.datetime(2015, 9, 16, 20, 30)
    game = DOM.Game("vvbteam1", "vvbteam3", date, "sportshall")
    league1.addGame(game)

    date = DT.datetime(2015, 9, 16, 20, 30)
    game = DOM.Game("vvbteam2", "vvbteam3", date, "sportshall")
    league1.addGame(game)

    res.append(league1)

    #second test league
    league2 = DOM.League("Liga B")

    date = DT.datetime(2015, 9, 15, 20, 30)
    game = DOM.Game("vvbteam1ligab", "vvbteam2ligab", date, "sportshall")
    league2.addGame(game)

    date = DT.datetime(2015, 9, 16, 20, 30)
    game = DOM.Game("vvbteam1ligab", "vvbteam3ligab", date, "sportshall")
    league2.addGame(game)

    date = DT.datetime(2015, 9, 16, 20, 30)
    game = DOM.Game("vvbteam2ligab", "vvbteam3ligab", date, "sportshall")
    league2.addGame(game)

    res.append(league2)

    return res





def testLS2():
    res = []
    league1 = DOM.League("1e provinciale")

    date = DT.datetime(2015, 9, 15, 20, 30)
    game = DOM.Game("avfteam1", "avfteam2", date, "sportshall")
    league1.addGame(game)

    date = DT.datetime(2015, 9, 16, 20, 30)
    game = DOM.Game("avfteam1", "avfteam3", date, "sportshall")
    league1.addGame(game)

    date = DT.datetime(2015, 9, 16, 20, 30)
    game = DOM.Game("avfteam2", "avfteam3", date, "sportshall")
    league1.addGame(game)

    res.append(league1)

    return res
