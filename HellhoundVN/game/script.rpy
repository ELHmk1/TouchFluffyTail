# You can place the script of your game in this file.

# Defines backgrounds we'll use
image bg outside:
    "assets/backgrounds/outside_bg.png"

# Defines sprites we'll use
#The c_ prefix denotes Fia's Hotpants Outfit
#The s_ prefix denotes Fia's Sweater Outfit
#The n_ prefix denotes Fia in the nude
#A 'w' in the prefix denotes a wet version
#The _u suffix denotes the fact Fia's tail is raised

#All the clothed sprites
image fia c_fire:
    #Actual Image File
    "assets/sprites/fia_clothed_grin.png"
    
    #Zoom stuff so it fits
    #zoom 0.55

image fia c_neutral:
    "assets/sprites/fia_clothed_neutral.png"
    #zoom 0.55

image fia c_smile:
    "assets/sprites/fia_clothed_smile.png"
    #zoom 0.55

image fia cw_pout:
    "assets/sprites/fia_clothedwet_pout.png"
    #zoom 0.55

#All the nude sprites
image fia n_smile:
    "assets/sprites/fia_nude_smile.png"
    #zoom 0.55
    
image fia nw_smile:
    "assets/sprites/fia_nudewet_smile.png"
    #zoom 0.55

#All the sweater sprites
image fia s_bite:
    "assets/sprites/fia_sweater_lipbite.png"
    #zoom 0.55

# Define the characters we'll use
#Fia
define f = Character('Fia', color="#c8ffc8", what_prefix='"', what_suffix='"')

#The MC
#As his inner thoughts will be handled by the narrator, we need to add quotes
define mc = Character("Mike", what_prefix='"', what_suffix='"')

# The acutal game starts here.
label start:
    #Set up two flags. First for the rain and second for slow sex
    $ flag_one = False
    $ slow = False
    
    #Start the VN with Fia & the MC outside
    scene bg outside
    show fia c_smile
    f "We're outside!"

    #First choice. Determines how fast they head home and how wet they get.
    menu:
        "Delay":
            jump lots_rain
        
        "No Delay":
            jump little_rain
            
    #We shouldn't ever get here but just in case...
    return

label lots_rain:
    #Set the first flag
    $ flag_one = True
    
    show fia cw_pout with fade
    f "I'm soaked!"
    #Move to the Apartment Scene
    jump apartment

label little_rain:  
    show fia c_neutral with fade
    f "We got inside just in time!"
    jump apartment

label apartment:
    scene bg apartment
    #Check how long they were out in the rain and fill in based on that
    if flag_one:
        show fia cw_pout
    else:
        show fia c_fire
    f "Apartment Time!"

    #Second choice. Determines how hard Fia goes at him
    menu:
        "Take a Shower":
            jump shower
    
        "Build an Awesome Fort":
            jump fort

#The beginnings of the Shower Scene
label shower:
    scene bg shower
    show fia nw_smile
    f "I'm going to enjoy playing with my bone~"

    #Third choice. Does the MC want to go slower?
    if flag_one:
        menu:
            "Let's slow down a little~":
                $ slow = True
                jump fort_two
            "Give her what she wants!":
                jump shower_two
    else:
        jump shower_two

#Actual shower scene
label shower_two:
    show fia nw_smile
    f "We're going to steam up the glass~"
    jump end_one

#First Ending (After the Shower)
label end_one:
    show fia n_smile
    f "I guess I got a LITTLE carried away"
    mc "You think?"
    return

#The Beginnings of the Fort Scene
label fort:
    scene bg fort
    show fia s_bite
    f "I'm going to build this fort then fuck you in it."
    jump fort_two
    
#The Actual Fort Scene
label fort_two:
    #If we're coming from the shower, do some prework
    if slow:
        show fia n_smile
        f "Alright lover boy. We'll do it your way."
        f "But not because I love you or anything!"
        scene bg fort
    f "Slow sex is best sex."
    jump end_two

#Second Ending (After Fort)
label end_two:
    show fia n_smile
    f "So much for doing anything this weekend~"
    return