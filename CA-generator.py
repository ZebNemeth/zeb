"""

Elementaire-cellulaire-automataplaatjesgenerator
Geef hem je regelnummer en resolutie en klaar is kees!


"""

import random
from PIL import Image


# Physics creation, see "Wolfram Code for elementary CA"

stateSpace = "L"     # string:   L for grayscale; not sleek yet.
                     #           1 for "binary". Not sleek yet; 0 and 255...
                     #           RGB for (0-255,",")

state = (255, 0)
rule = [ state[0],   # 111
         state[1],   # 110
         state[1],   # 101
         state[0],   # 100
         state[1],   # 011
         state[0],   # 010
         state[1],   # 001
         state[0]    # 000
         ]

# Environment creation

imageWidth = 1920
imageHeight = 1080

imgCA = Image.new( stateSpace, [imageWidth, imageHeight], 130) # 130; fill gray
cell = imgCA.load()


# Fill the initial state

for x in range (0, imageWidth):
   cell[x,0] = random.choice(state)




# Evolve the universe

for y in range (1, imageHeight):
   for x in range (0, imageWidth):


      # Trying not to let image index go out of range on the edges of the image
      if ( x == 0 ):
         parents = ( cell[imageWidth-1, y-1], cell[x, y-1], cell[x+1, y-1] )
      elif ( x == imageWidth-1 ):
         parents = ( cell[x-1, y-1], cell[x, y-1], cell[0, y-1] )
      else:
         parents = ( cell[x-1, y-1], cell[x, y-1], cell[x+1, y-1] )



      if   ( parents == (state[0],state[0],state[0]) ):
         cell[x,y] = rule[7]
      elif ( parents == (state[0],state[0],state[1]) ):
         cell[x,y] = rule[6]
      elif ( parents == (state[0],state[1],state[0]) ):
         cell[x,y] = rule[5]
      elif ( parents == (state[0],state[1],state[1]) ):
         cell[x,y] = rule[4]
      elif ( parents == (state[1],state[0],state[0]) ):
         cell[x,y] = rule[3]
      elif ( parents == (state[1],state[0],state[1]) ):
         cell[x,y] = rule[2]
      elif ( parents == (state[1],state[1],state[0]) ):
         cell[x,y] = rule[1]
      elif ( parents == (state[1],state[1],state[1]) ):
         cell[x,y] = rule[0]

imgCA.show()
