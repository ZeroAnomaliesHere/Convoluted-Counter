import random
import sys
import textwrap

def Conv_Counter():
  correct_count = False
  num_of_iters = 0
  total_restarts = 0
  highest_num = 0 
  intro = "  It's only goal is to count to a number of your choosing from 0. There is a catch though, the program has to roll a random number from 0 to the number of your choice, and it has to be in successive order. Meaning that it has to land on 0, then 1, 2, 3, and so on or else it restarts!\n"

  # Not 100% sure, but I think this wraps the intro text
  wrapper = textwrap.TextWrapper(width=50)
  intro_text = wrapper.fill(text = intro)

  print("This is the Convoluted Counter by Fulminare!\n")
  print(intro_text + "\n")

  max = int(input("What number would you like to count to? "))
  
  while correct_count == False:
    counting = True
    current = 0
  
    total_restarts = total_restarts + 1

    while counting == True:
      num_of_iters = num_of_iters + 1
      rand = random.randint(0, max)
      current = current + 1 

      
      sys.stdout.write("\rIt's taken %s tries to get to %s, onto %s" % (total_restarts, highest_num, highest_num + 1) + "!")
      sys.stdout.flush()
      
      if current > highest_num: # Shows the progression
        highest_num = current
        print("")
        
      if rand != current + 1: # See if it breaks chain
        counting = False
        
      if current == max: # It finised!
        print("\nWe managed to get to %s" % max + "! It only took %s iterations." % total_restarts)
        return 
      

Conv_Counter()
