# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image fia test:
    #Actual Image File
    "fia_test.png"
    
    #Zoom stuff so it fits
    zoom 0.85
    
# Declare characters used by this game.
#Defines Fia
define f = Character('Fia', color="#c8ffc8", what_prefix='"', what_suffix='"')

#Defines the MC
define mc = Character("[mcname]")

# The game starts here.
label start:
    #See if the player wants to use their own name
    python:
        mcname = renpy.input("What is your name? Leave empty for default.")
        mcname = mcname.strip()

        if not mcname:
            mcname = "Mike"

    show fia test at right
    f "Hi [mcname]~"

    f "Hurry up and code the rest of my dialogue!"

    return
