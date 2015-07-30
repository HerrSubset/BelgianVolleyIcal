## This file contains all the scripts used to download information from the
## web and transform it to usable python data objects. These scripts are mainly
## used by the federation classes in the file domain.py

import datetime as DT
import domain as DOM

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
    league1.addGame(game)

    res.append(league2)

    return res





def testLS2():
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
