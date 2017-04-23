# "Castle Trap" was inspired by my five year old son.
# He has a better imagination than I do, so I asked for his help.

from sys import exit
import random

def prompt():
    print
    choice = raw_input("What do you do? ")
    return choice

def basement():
    choice = ""
    print """
    You are in a dank, dark dungeon.
    Behind you is what appears to be the bottom of a slide.
    You can see a large, red button on the far wall.
    """
    #prompt()
    choice = prompt()

    if "red" in choice or "button" in choice:
        print "The slide turns into a set of stairs leading up to the ceiling"
        choice = prompt()
        if "climb" in choice or "stairs" in choice:
            trap_door()
        else:
            if "button" in choice:
                print "The stairs turn into a slide."
                basement()
            else:
                "What are you even talking about?"
                basement()
    elif "slide" in choice:
        print "The slide is too slippery to climb, even with super sticky sneakers."
        basement()
    else:
        print "What the heck are you even talking about?!?!?!"
        basement()

def trap_door():
    print "At the top of the stairs, you find a trap door in the ceiling."
    choice = prompt()

    if "open" in choice:
        room1()
    else:
        print "Are you sure you know how to play this game?"
        trap_door()

def room1():
    print """
    You are in an empty room.
    The only item of any note is a door knob on what seems to be a solid wall.
    """
    choice = prompt()
    if "knob" in choice:
        print "A hidden door opens out into the great hall beyond."
        bear()
    else:
        print "You need to try something else."
        room1()

def bear():
    print "You hear the unmistakeable growl of a grizzly bear coming from across the hall."
    result = random.randint(1, 4)
    #print result
    if result == 4:
        print """
        Because you were so frightened by the sound of the bear,
        you suffered a massive heart attack and died on the spot.
        The end.
        """
        exit(0)
    elif result == 3:
        print """
        This is just crazy. What happens is that
        a giant vacuum plant comes down from the ceiling
        of the great hall and vacuums you up!
        Eventually, you work your way down the stem
        and are dropped back down the trap door in the empty room.
        The stairs have converted back to a slide and you slide down.
        """
        basement()
    else:
        print """
        You see a way out of the great hall down a corridor that
        leads away from the bear. This is good, because the bear is
        figuring out how to open its cage!!
        """
        result = random.randint(1, 4)
        #print result
        choice = prompt()
        if "corridor" in choice or "run" in choice:
            print "Good thinking!"
            if result == 4:
                bearMeal()
            else:
                boulder()
        else:
            print "Dude. Come on now. That bear looks hungry!"
            bear()

def boulder():
    print "You are moving down the corridor."
    result = random.randint(1, 4)
    #print result
    if result == 4:
        bearMeal()
    else:
        print """
        What is this crazy place? Listen to what happens next.
        You see that the way ahead is blocked by a giant boulder.
        There is a worn-out spot on the carpet near the boulder.
        Looking closer at this, you determine it is some kind of foot button.
        """
        choice = prompt()

        if "button" in choice:
            print """
            Sound thinking, Tex! But you just will not believe what happens next!
            As you step on the button on the floor, you notice a giant robot arm
            swing out from the wall to your right.
            It grabs onto a rope and gives it a mighty yank.
            The rope runs to a pulley hidden up near the ceiling and then down to
            the boulder. Pulling the rope releases the boulder, which falls
            through the floor and crashes through the castle. It then crashes
            through the floor of the great hall and lands with a thunderous
            crash in the dungeon. What the heck!?!?!?!
            """
            lock()
        else:
            print "Seriously? You can't figure out what to do?"
            boulder()

def lock():
    print """
    Making your way past the very strange boulder trap...which semeed to just
    wreck up the castle and not really trap you at all...you round the bend and
    come upon a door with a big lock on it. The good news is that the key is in
    the lock! The bad news is that you can hear the bear back down the corridor,
    and he is getting closer!
    """
    choice = prompt()
    result = random.randint(1, 4)
    #print result
    if result == 4:
        bearMeal()
    elif "lock" in choice or "key" in choice:
            print """
            Wise move. The lock falls to the floor with a thud and the door
            swings open.
            """
            gold()
    else:
        print "Holy crows, man! Figure it out!"
        lock()

def gold():
    print "You found the treasure room! It is teaming with gold!"
    choice = prompt()
    result = random.randint(1, 4)
    #print result
    if result == 4:
        bearMeal()
    elif "gold" in choice:
        print """
        You fill your pockets with gold and see a window that you can
        escape out of. Not wanting to face a bear, or any of the other crazy
        things in this weird castle, you jump out the window and run away home.
        Because you now have a great deal of gold, you have no more worries
        and you and your family live happily ever after.
        The end.
        """
        exit(0)

def bearMeal():
    print """
    Too late!
    The bear got you before you could escape!
    You are inside a grizzly bear stomach.
    It is dark and smelly, but you don't mind...
    because you are dead.
    The end.
    """
    exit(0)


print """


       _..._
    .-'_..._''.                             .---.
  .' .'      '.\                            |   |      __.....__                                 _________   _...._
 / .'                                       |   |  .-''         '.                               \        |.'      '-.
. '                                     .|  |   | /     .-''"'-.  `.       .|  .-,.--.            \        .'```'.    '.
| |                 __                .' |_ |   |/     /________\   \    .' |_ |  .-. |    __      \      |       \     \
| |              .:--.'.         _  .'     ||   ||                  |  .'     || |  | | .:--.'.     |     |        |    |
. '             / |   \ |      .' |'--.  .-'|   |\    .-------------' '--.  .-'| |  | |/ |   \ |    |      \      /    .
 \ '.          .`" __ | |     .   | / |  |  |   | \    '-.____...---.    |  |  | |  '- `" __ | |    |     |\`'-.-'   .'
  '. `._____.-'/ .'.''| |   .'.'| |// |  |  |   |  `.             .'     |  |  | |      .'.''| |    |     | '-....-'`
    `-.______ / / /   | |_.'.'.-'  /  |  '.''---'    `''-...... -'       |  '.'| |     / /   | |_  .'     '.
             `  \ \._,\ '/.'   \_.'   |   /                              |   / |_|     \ \._,\ '/'-----------'
                 `--'  `"             `'-'                               `'-'           `--'  `"

Designed by Calin Matthew Hannan
Written by Daddy Matthew Hannan
22 April 2017
"""

basement()
