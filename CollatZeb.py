"""

 Collatz-conjecture stappenteller tussen machten van tien
 Zeb Nemeth 13 december 2019
 
 Collatz-iteratie:
 Positief geheel getal: Even? Deel door twee.
                        Oneven? Maal drie, plus één.

 Kom je altijd terug van n, n/2, ...tot 1?

"""


def CollatzTeller(MachtBegin, MachtEinde):
   if (MachtBegin < 0):
      return ("Error: starting power < 0 (now: %d)" % (MachtBegin))
   elif (MachtEinde <= MachtBegin):
      return ("Error: ending power (%d) lower than starting power (%d)" % (MachtEinde, MachtBegin))
   
   Getal = 10**MachtBegin
   Eindtal = 10**MachtEinde


   WerkGetal = Getal
   StappenTel = 0
   HoogsteTel = StappenTel


   while (Getal != Eindtal):

      while (WerkGetal != 1):

         if (WerkGetal % 2 == 1):
            WerkGetal *= 3
            WerkGetal += 1
            StappenTel += 1
         else:
            WerkGetal = (WerkGetal // 2)
            StappenTel += 1

         if (StappenTel >= HoogsteTel):
            HoogsteTel = StappenTel
            HoogsteTal = Getal

      StappenTel = 0
      Getal += 1
      WerkGetal = Getal


   return (HoogsteTel, HoogsteTal)
# Einde CollatzTeller( MachtBegin, MachtEinde )

"""
# Voorbeeldgebruik en -foutmeldingen

for i in range ( 0, 5 ):
  print( CollatzTeller( i, i+1 ) )

print( CollatzTeller( -1, 2 ) ) # Errorcheck negatieve beginmacht
print( CollatzTeller( 0, 4 ) )   # Gaat goed
print( CollatzTeller( 3, 4 ) )   # Gaat goed, zelfde resultaat
print( CollatzTeller( 3, 2 ) )   # Gaat niet goed, begin hoger dan eind
"""