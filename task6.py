# task : 1 List all possible outcomes (sample space) for rolling a standard six-sided die and flipping a coin at the same time.
#             Write your answer as a list of ordered pairs.

"""
six - sided die : possible outcomes == 1,2,3,4,5,6
one coin :  possible outcomnes == HEAD, TAIL 

The probability of ordered pairs(die, coin) :

P = {(1,H) , (1,T) , (2,H) , (2,T) , (3,H) (3,T) , (4,H) , (4,T) ,(5,H) ,(5,T) , (6,H) , (6,T) }

TOTAL PROBABILITY : 12 PAIRS OF DIE , COIN 

"""

# TASK : 2 Suppose you have a deck of 10 cards numbered 1 to 10. Calculate the classical probability of drawing a card with an even number. 
#          Show your calculation steps.

"""
claculate probability of drawing an even number:

total number of cards : 10 
even numbered cards :  2, 4, 6, 8, 10. == 5 even number cards 

probaility of even number cards [P(A)] =   favorable outcomes / Total outcoms 
                                P(A) = 5/10 
                                     = 0.5 

"""
# Task : 3 In a playlist of 8 songs on Spotify, 3 are by Arijit Singh. If you shuffle and play one random song, what is the probability that it is NOT by Arijit Singh? Show your working.

"""
total songs : 8 
songs by Arijit Singh : 3 
songs NOT by Arijit Singh : 8 - 3 = 5 

probability of NOT drawing a song by Arijit Singh [P(A')] =   favorable outcomes / Total outcoms 
                                                                P(A') = 5/8 
                                                                     = 0.625 

"""

# Task : 4 A Zomato user places an order. The probability they order Pizza is 0.3, and the probability they order Burger is 0.4. 
# If the probability they order both is 0.1, use the addition rule to find the probability the user orders Pizza or Burger.<br><br><em><strong>Hint:</strong> P(A or B) = P(A) + P(B) - P(A and B)</em>
"""
P(a) (pizza) = 0.3 
P(b) (burger) = 0.4
P(a and b) = 0.1

probability of ordering pizza or burger [P(A or B)] = P(A) + P(B) - P(A and B)
      P(A or B) = 0.3 + 0.4 - 0.1
      P(A or B) = 0.6
"""

# Task : 5 A Flipkart user is browsing electronics. The probability they add a phone to cart is 0.2. If you know they are interested in mobiles, the probability rises to 0.5. 
#          Briefly explain in your own words what this conditional probability means, using this scenario.
""""

Conditional probability is the probability of an event happening when we already know that another event has occurred.
In this scenario, 
   the probability of a Flipkart user adding a phone to their cart is 0.2 (20%).
   when we add a phone than the probability of adding a phone to the cart increases to 0.5 (50%) that we know that the user is interested in mobiles.
   
"""