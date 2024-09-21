from pickle import *
class Team:
    def __init__(self, string):
        self.info = string.split(',')
        self.group = self.info[0]
        self.team_name = self.info[1]
        self.matches = int(self.info[2])
        self.won = int(self.info[3])
        self.draw = int(self.info[4])
        self.loss = int(self.info[5])
        self.goals_for = int(self.info[6])
        self.goals_against = int(self.info[7])
        self.goals_difference = int(self.info[8])
        self.points = int(self.info[9])

    def __str__(self):
        #f string format used to align columns
        string = self.info[0] + '\t' + f'{self.info[1]:<15}'
        for i in range(2, 10):
            string += f'{self.info[i]:>5}'#f string format used to maintain width of columns
        return string.strip()
class Tournament:
    def __init__(self, file):
        self.teams = []
        file.readline() #read heading and ignore to move pointer to first team record
        for i in range(32):
            self.teams.append(Team(file.readline().strip()))
    def __str__(self):
        string = ''
        for team in self.teams:
            string += str(team) + '\n'
        return string

file = open('fifa.csv', 'r')
tournament = Tournament(file)
file.close()
string = dumps(tournament) #transform object into string
print (string)
input('\nRead serialization string and press enter to see next output')
print() #leave a blank line
tournament1 = loads(string) #transform string into object
print (tournament1)