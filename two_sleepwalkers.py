# A version of two sleepwalker animation racing to the walls


import time
import random

def rs():
    """ One random step """
    return random.choice([-1, 1])

def flash(Mbappe, Rashford, FINISH):   #two of the fastest footballers of this generation as variables
    """ Two of the fastest footballers drunk race to the finish line """
    run = 0
    low = 0
    high = 30

    while True:            
        if Mbappe == FINISH or Rashford == FINISH:  
            return run 
        elif Mbappe <= 0 or Rashford <= 0:
            return run 
        elif Mbappe >= 30 or Rashford >= 30: 
            return run
        elif Mbappe != Rashford:
          Mbappe += rs()
          Rashford += rs()
          run += 1

        left = Mbappe - low
        middle = Rashford - Mbappe
        right = high - Rashford

        print("🏁" + "➖"*left + "🏃🏾" + "➖"*middle + "🏃" + "➖"*right + "🏁",flush= True)
        time.sleep(0.042)

#test
flash(5,15,10)