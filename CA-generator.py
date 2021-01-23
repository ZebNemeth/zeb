"""
   Zeb Nemeth
   januari 2020


Elementaire-cellulaire-automataplaatjesgenerator
Geef hem je (regelnummer, dichtheid, breedte, hoogte) 
en klaar is kees!


"""

import random
from PIL import Image
import time

beginCPUCycle = time.time() # om efficientere code te testen







def GenerateImage(ruleWolframCode, density, imageWidth, imageHeight):

   # Physics creation, see "Wolfram Code for elementary CA"
   """
   hier kan nog veel aan gesleuteld worden voor multifunctionaliteit
   """
   stateSpace = "L"     # string:   L for grayscale; not sleek yet.
                        #           1 for "binary". Not sleek yet; 0 and 255...
                        #           RGB for (0-255,",")
   stateAmount = 2

   parentAmount = 3

   state = (255, 0)


   # Binarification, rule given

   binaryRuleWolframCode = [0]*8
   for i in range (7, -1, -1):
      binaryPower = 2**i
      a = ruleWolframCode - binaryPower
      if ( a >= 0 ):
         ruleWolframCode -= binaryPower
         binaryRuleWolframCode[i] = 1
         print (ruleWolframCode)
      else:
         binaryRuleWolframCode[i] = 0
   print ( binaryRuleWolframCode )

   rule = [ state[binaryRuleWolframCode[0]],   # 000    ...namely binary parent description
            state[binaryRuleWolframCode[1]],   # 001
            state[binaryRuleWolframCode[2]],   # ..
            state[binaryRuleWolframCode[3]],
            state[binaryRuleWolframCode[4]],
            state[binaryRuleWolframCode[5]],
            state[binaryRuleWolframCode[6]],
            state[binaryRuleWolframCode[7]]    # 111
            ]



   # Environment creation, width and height given

   imgCA = Image.new( stateSpace, [imageWidth, imageHeight], 130) # 130; fill gray
   cell = imgCA.load()





   # Fill the initial state. density given

   for x in range (0, imageWidth):
      cell[x,0] = random.randint(0,255)
      if ( cell[x,0] < int(density*255) ):
         cell[x,0] = state[1]
      else:
         cell[x,0] = state[0]






   # Evolve the universe

   for y in range (1, imageHeight):
      for x in range (0, imageWidth):


         # Trying not to let image index go out of range on the edges of the image
         if ( x == 0 ):
            cell[x,y] = rule[ 4 * ( cell[imageWidth-1, y-1] == state[1] ) +
                              2 * ( cell[x, y-1] == state[1] ) +
                              ( cell[x+1, y-1] == state[1] )
                           ]
         elif ( x == imageWidth-1 ):
            cell[x,y] = rule[ 4 * ( cell[x-1, y-1] == state[1] ) +
                              2 * ( cell[x, y-1] == state[1] ) +
                              ( cell[0, y-1] == state[1] )
                           ]
         else:
            cell[x,y] = rule[ 4 * ( cell[x-1, y-1] == state[1] ) +
                              2 * ( cell[x, y-1] == state[1] ) +
                              ( cell[x+1, y-1] == state[1] )
                           ]

   imgCA.show()

GenerateImage(110,.5,1000,1000)

print ( time.time() - beginCPUCycle )