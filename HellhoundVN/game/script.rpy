# Main script of the game

# Defines backgrounds we'll use
image bg outside = "assets/backgrounds/outside_bg.png"
image bg shower = "assets/backgrounds/bathroom_bg.png"
image black = Solid((0, 0, 0, 255))

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

image fia c_pout:
    "assets/sprites/fia_clothed_pout.png"

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
define f = Character('Fia', color="#f25000", what_prefix='"', what_suffix='"')

#The MC
#As his inner thoughts will be handled by the narrator, we need to add quotes
define mc = Character("Mike", what_prefix='"', what_suffix='"')

#Transitions and variables
init:
    #Remember to inflate the iris to be 1920x1080!
    $ circirisout = ImageDissolve("assets/backgrounds/circleiris.png", 1.0, 8)
    $ circirisin = ImageDissolve("assets/backgrounds/circleiris.png", 1.0, 8, reverse=True)
    $ flag_one = False
    $ slow = False

# The acutal game starts here.
label start:
    #Set up two flags. First for the rain and second for slow sex
    
    #Start the VN with Fia & the MC outside
    scene black
    "..."
    "I've lost track of the time again..."
    "But maybe that was the whole point of all this."
    "After all, it's not often that Fia and I have time to truly relax."
    "That's why we're staying around town this Spring Break."
    "???" "...ike."
    "???" "MIKE."
    "Perhaps I spoke too soon about being able to relax..."
    
    #Open his eyes
    #REPLACE THIS WITH CIRCLEIRIS ASAP
    scene bg outside with circirisout
    #Anytime she changes sprites add "with dissolve"
    show fia c_pout with dissolve
    "As I open my eyes, I'm greeted with the sight of my girlfriend looming over me."
    "We had been out for a stroll when we decided to rest under the sun."
    "This far out in the hills there's plenty of nice fields and trees for just such a purpose."
    "Though, judging by her expression, it seems Fia's tired of laying about."
    f "Jeez."
    f "I've been trying to wake you up for at least five minutes now!"
    mc "Sorry about that. Did something happen?"
    show fia c_neutral with dissolve
    f "Maybe. Take a look over there."
    "She points over my shoulder at the sky behind us."
    "At first I struggle to see what she's talking about. The crystal blue sky seems as normal as ever."
    "But then I notice a glint of light."
    "The longer I stare at it the more it seems serpentine in nature. Is that a Ryu?"
    mc "I didn't know you were into Dragon-Watching, Fia."
    show fia c_pout with dissolve
    f "I'm not!"
    "If I didn't know any better, I'd tease her about being overprotective again."
    "She's gotten better at it but she can't help the nature of her race."
    mc "Alright, why the concern over a Ryu then?"
    show fia c_neutral with dissolve
    f "Well you know how they are. Control over the weather and all that."
    f "I just thought that if there's one swimming about up there, we might be due for some rain."
    "She's not entirely wrong. Usually you can predict when it'll rain by watching for certain Monstergirl types."
    "Though then again..."
    mc "Maybe she's just having fun? Or maybe on her way to see her boyfriend?"
    f "Maybe..."
    "Her eyes shift away from me ever so slightly, focusing instead on the Ryu."
    "I can't fault her for worrying about it. Her current outfit is rather... susceptible to moisture."
    "Plus she hates getting wet outside of showers and baths. Those, for some reason, she absolutely loves."
    "It's an odd quirk, but it's one of many I've come to accept about her."
    mc "Well if you're that worried, should we head back?"
    f "We'd be cutting our walk short then..."
    "It's hard to tell whether she's genuinely disappointed. Especially since her usual tell, her tail isn't giving me any clues."
    "So instead, I opt for a joke."
    mc "Because we were totally not doing that sleeping here."
    show fia c_smile with dissolve
    "Finally she shows a hint of a smile. Even her tail wags a little."
    f "Fair enough."
    "Her eyes do dart back to the Ryu once more though."
    "Maybe we should head back to our apartment?"

    #First choice. Determines how fast they head home and how wet they get.
    menu:
        "Don't go back just yet":
            jump lots_rain
        
        "Head straight home":
            jump little_rain
            
    #We shouldn't ever get here but just in case...
    return

label lots_rain:
    #Set the first flag
    $ flag_one = True
    
    show fia cw_pout with dissolve
    f "I'm soaked!"
    #Move to the Apartment Scene
    jump apartment

label little_rain:  
    show fia c_neutral with dissolve
    f "We got inside just in time!"
    jump apartment

label apartment:
    scene bg apartment with fade
    #Check how long they were out in the rain and fill in based on that
    if flag_one:
        show fia cw_pout with dissolve
    else:
        show fia c_fire with dissolve
    f "Apartment Time!"

    #Second choice. Determines how hard Fia goes at him
    menu:
        "Take a Shower":
            jump shower
    
        "Build an Awesome Fort":
            jump fort

#The beginnings of the Shower Scene
label shower:
    scene bg shower with fade
    show fia nw_smile with dissolve
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
    show fia nw_smile with dissolve
    f "We're going to steam up the glass~"
    jump end_one

#First Ending (After the Shower)
label end_one:
    show fia n_smile with dissolve
    f "I guess I got a LITTLE carried away"
    mc "You think?"
    return

#The Beginnings of the Fort Scene
label fort:
    scene bg fort with fade
    show fia s_bite with dissolve
    f "I'm going to build this fort then fuck you in it."
    jump fort_two
    
#The Actual Fort Scene
label fort_two:
    #If we're coming from the shower, do some prework
    if slow:
        show fia n_smile with dissolve
        f "Alright lover boy. We'll do it your way."
        f "But not because I love you or anything!"
        scene bg fort with fade
    f "Slow sex is best sex."
    jump end_two

#Second Ending (After Fort)
label end_two:
    show fia n_smile with dissolve
    f "So much for doing anything this break~"
    return