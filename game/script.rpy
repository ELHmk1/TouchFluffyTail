# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
#Defines Fia
define f = Character('Fia', color="#c8ffc8", what_prefix='"', what_suffix='"')

#Defines the MC
define mc = Character("[povname]")

# The game starts here.
label start:
    python:
        povname = renpy.input("What is your name? Leave empty for default.")
        povname = povname.strip()

        if not povname:
            povname = "Marcus"
    mc "My name is [povname]!"
    f "You've created a new Ren'Py game."

    f "Once you add a story, pictures, and music, you can release it to the world!"

    return
