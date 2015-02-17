# You can place the script of your game in this file.

# Defines images we'll use
#The c_ prefix denotes Fia's Hotpants Outfit
#The s_ prefix denotes Fia's Sweater Outfit
#The n_ prefix denotes Fia in the nude
#A 'w' in the prefix denotes a wet version
#The _u suffix denotes the fact Fia's tail is raised

#All the happy images
image fia c_happy:
    #Actual Image File
    "Art/c_happy.png"
    
    #Zoom stuff so it fits
    zoom 0.85

image fia n_happy_u:
    "Art/n_happy_u.png"
    zoom 0.85

#All the neutral images
image fia s_neutral:
    "Art/s_neutral.png"
    zoom 0.85

image fia wn_neutral:
    "Art/wn_neutral.png"
    zoom 0.85

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
    show fia c_happy at right
    f "We're outside!"

    #First choice. Determines how fast they head home and how wet they get.
    menu:
        "Delay":
            jump lots_rain
        
        "No Delay":
            jump little_rain
    
    label lots_rain:
        #Set the first flag
        $ flag_one = True
        
        show fia wn_neutral
        f "I'm soaked!"
        #Move to the Apartment Scene
        jump apartment
    
    label little_rain:        
        f "We got inside just in time!"
        jump apartment

    label apartment:
        scene bg apartment
        #Check how long they were out in the rain and fill in based on that
        if flag_one:
            show fia wc_happy at right
        else:
            show fia c_happy at right
        f "Pomf!"
        f "What are we going to do in the apartment, Mike?"

        #Second choice. Determines how hard Fia goes at him
        menu:
            "Take a Shower":
                jump shower
        
            "Build an Awesome Fort":
                jump fort

        #The beginnings of the Shower Scene
        label shower:
            scene bg shower
            show fia wn_neutral at right
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
            show fia wn_neutral at right
            f "We're going to steam up the glass~"
            jump end_one
        
        #First Ending (After the Shower)
        label end_one:
            show fia n_happy_u at right
            f "Don't think that you're off the hook yet!"
            return
        
        #The Beginnings of the Fort Scene
        label fort:
            scene bg fort
            show fia s_neutral at right
            f "I'm going to build this fort then fuck you in it."
            jump fort_two
            
        #The Actual Fort Scene
        label fort_two:
            #If we're coming from the shower, do some prework
            if slow:
                show fia n_happy_u at right
                f "Alright lover boy. We'll do it your way."
                f "But not because I love you or anything!"
                scene bg fort
            f "Slow sex is best sex."
            jump end_two
        
        #Second Ending (After Fort)
        label end_two:
            show fia n_happy_u at right
            f "I hope you didn't have plans this weekend."
            mc "Huh?"
            "She giggles, pulling me closer."
            f "We're not leaving this fort until were an absolute mess~"
            mc "Uh oh."
            return
    return
