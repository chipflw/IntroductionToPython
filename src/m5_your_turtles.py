"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Chip Daniel.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(20)


size = 20

for k in range(10):

  sam= rg.SimpleTurtle()
  sam.pen = rg.Pen('green', 5)
  sam.speed = 1000
  sam.draw_regular_polygon(8,size)

  ben= rg.SimpleTurtle()
  ben.pen = rg.Pen('blue', 5)
  ben.speed = 1000
  ben.draw_regular_polygon(8,size + 3)
  size = size + 10

  nick= rg.SimpleTurtle()
  nick.pen = rg.Pen('red', 5)
  nick.speed = 1000
  nick.draw_regular_polygon(8, size + 6)




