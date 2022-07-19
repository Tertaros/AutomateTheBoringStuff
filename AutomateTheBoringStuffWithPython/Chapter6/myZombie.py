import zombiedice, random

class Zombie1:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        while diceRollResults is not None:
            coinflip = random.randint(0,1)
            if(coinflip == 0):
                diceRollResults = zombiedice.roll()
            else:
                break


class Zombie2:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class Zombie3:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        shotgunRolled = 0
        while diceRollResults is not None:
            shotgunRolled += diceRollResults['shotgun']
            if shotgunRolled != 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break


class Zombie4:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        shotgunRolled = 0
        turn = 0
        numberofTurns = random.randint(0,3)

        while diceRollResults is not None:
            if turn > numberofTurns:
                break
            turn += 1
            shotgunRolled += diceRollResults['shotgun']
            #print('Shotgun rolls: ' +  str(shotgunRolled))
            if shotgunRolled == 2:
                break
            diceRollResults = zombiedice.roll()


class Zombie5:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        while diceRollResults is not None:
            shotgunRolled = 0
            brains = 0
            shotgunRolled += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            #print('Shotguns: ' + str(shotgunRolled))
            #print('Brains : ' + str(brains))
            if shotgunRolled <= brains:
                diceRollResults = zombiedice.roll()
            else:
                break

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        shotgunsRolled = 0
        turn = 0

        #BOT that after the first roll, randomly decides if it will continue or stop
        while diceRollResults is not None:
            coinflip = random.randint(0,1)
            if(coinflip == 0):
                diceRollResults = zombiedice.roll()
            else:
                break


        '''
        while diceRollResults is not None:
            turn += 1
            brains += diceRollResults['brains']
            shotgunsRolled += diceRollResults['shotgun']
            #print(diceRollResults)
            #print('Turn: ' + str(turn))
            #print('Shotguns: ' + str(shotgunsRolled))
            #print('Brains : ' + str(brains))
            #print('')

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            elif shotgunsRolled == 2 and brains == 0:
                diceRollResults = zombiedice.roll()
            else:
                #print('Stopped Playing')
                break
        '''

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='Thomas Zombie Bot'),
    Zombie1(name='Zombie that randomly decides'),
    Zombie2(name='Zombie that stops after getting two 2 brains'),
    Zombie3(name='Zombie that stops after getting shot twice'),
    Zombie4(name='Zombie that initially decides it’ll attack one to four times, but will stop early if it gets shot twice'),
    Zombie5(name='Zombie that stops attacking after getting more shot at than receving brains')

    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
