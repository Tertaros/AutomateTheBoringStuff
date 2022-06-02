# Coin Flip Streaks

import random
numberOfStreaks = 0

for experimentNumber in range(10000):

    # Generating coin tosses
    coinTosses = []

    for i in range(100):
        coinTossResult = random.randint(0,1)
        if(coinTossResult==0):
            coinTosses.append('H')
        else:
            coinTosses.append('T')


    # Checking for streakings
    """
    prevResult = ''
    localStreak = 0
    for result in coinTosses:
        if(prevResult != result or prevResult == ''):
            prevResult = result
            localStreak = 1
        else:
           localStreak += 1

        if(localStreak==6):
            localStreak = 0
            numberOfStreaks += 1
    """
    for i in range(len(coinTosses)):
        if(i == 0):
            localStreak = 1
        elif(coinTosses[i-1]==coinTosses[i]):
            localStreak += 1
        else:
            localStreak = 0

        if(localStreak == 6):
            localStreak = 0
            numberOfStreaks += 1



print('Number of Six Heads or Tails Streaks: ' + str(numberOfStreaks))
print('Chance of streak: %s%%' % (numberOfStreaks / 100)) # %% is a conversation specifier
