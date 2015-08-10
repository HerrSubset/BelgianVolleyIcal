import loadScripts as LS

################################################################################
################################################################################
## calendarGenerator class
## This is the controller class to access all the available functionality
################################################################################
################################################################################
class calendarGenerator(object):
    def __init__(self):
        self.federations = []

        self.federations.append(Federation(LS.VVBLoadScript, "VVB"))


    #return the names of the available federations
    def getFederations(self):
        res = []

        for f in self.federations:
            res.append(f.getName())

        return res


    #return the names of the available leagues belonging to a certain federation
    def getLeagues(self, federation):
        res = None

        for f in self.federations:
            if f.getName() == federation:
                res = f.getLeagues()

        return res


    #return the team names that play in a certain league
    def getTeams(self, federation, league):
        res = None

        for f in self.federations:
            if f.getName() == federation:
                res = f.getTeams(league)

        return res


    #return the games that a certain team plays
    def getTeamCalendar(self, federation, league, team):
        res = None

        for f in self.federations:
            if f.getName() == federation:
                res = f.getTeamCalendar(league, team)

        return res





################################################################################
################################################################################
## Federation class
## The federation class holds one or more leagues.
################################################################################
################################################################################
class Federation(object):
    #constructor
    def __init__(self, loadScript, fedName):
        self.loadScript = loadScript
        self.fedName = fedName

        self.leagues = self.loadScript()


    #returns the federation name
    def getName(self):
        return self.fedName


    #returns the league names belonging to a federation
    def getLeagues(self):
        res = []

        for l in self.leagues:
            res.append(l.getName())

        return res


    #returns the teamnames playing in the given league
    def getTeams(self, league):
        res = None

        for l in self.leagues:
            if l.getName() == league:
                res = l.getTeams()

        return res


    #returns the calendar for the given team
    def getTeamCalendar(self, league, team):
        res = None

        for l in self.leagues:
            if l.getName() == league:
                res = l.getTeamCalendar(team)

        return res




################################################################################
################################################################################
## League class
## This class represents a league in a specific federation. It contains all the
## games that will be played in that league during a season.
################################################################################
################################################################################
class League(object):
    #constructor
    def __init__(self, name):
        self.name = name
        self.games = []


    #getters
    def getName(self):
        return self.name
    def getGames(self):
        return self.getGames


    #other Functions
    def addGame(self, game):
        self.games.append(game)


    #constructs and returns a list with all the team names
    def getTeams(self):
        res = []

        for g in self.games:
            if res.count(g.getHomeTeam()) == 0:
                res.append(g.getHomeTeam())
            if res.count(g.getAwayTeam()) == 0:
                res.append(g.getAwayTeam())

        return res


    #constructs the calendar for the given team
    def getTeamCalendar(self, team):
        res = []

        if self.getTeams().count(team) == 1:
            for g in self.games:
                if g.homeTeam == team or g.awayTeam == team:
                    res.append(g)

        return res




################################################################################
################################################################################
## Game class
## This class contains the information concerning one specific game.
################################################################################
################################################################################
class Game(object):
    #constructor
    def __init__(self, homeTeam, awayTeam, date, location):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.date = date
        self.location = location

    #getters
    def getHomeTeam(self):
        return self.homeTeam
    def getAwayTeam(self):
        return self.awayTeam
    def getDate(self):
        return self.date
    def getLocation(self):
        return self.location

    #other Functions
    def toString(self):
        return self.date.isoformat() + "\t" + self.homeTeam + " - " + self.awayTeam + "\t" + self.location
