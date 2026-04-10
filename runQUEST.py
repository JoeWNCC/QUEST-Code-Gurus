"""
    QUEST Game
    run QUEST file from here
"""

import QUEST

# You can preset some items in testing by using QUEST.item_name = x
# You may also change the location you start at by changing the code
# below to a method from the QUEST library. The starting area is
# QUEST.drab_town()

# EXAMPLE: QUEST.property_name = 0 or 1/true or false/"string value"
QUEST.Chef = 1
QUEST.Ally = "TONIO"
QUEST.Player_Name = "Brown"
QUEST.sword = 1
QUEST.Werewolf = True

# ! WARNING !
# If you preset the ally status for Chef and Rogue, their names will
# not show up properly

QUEST.ruins_2()