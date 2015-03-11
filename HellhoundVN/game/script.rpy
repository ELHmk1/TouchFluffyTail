# Main script of the game

# Defines backgrounds we'll use
image bg outside = "assets/backgrounds/outside_bg.png"
image bg shower = "assets/backgrounds/bathroom_bg.png"
image bg apartment = Placeholder("bg")
image black = Solid((0, 0, 0, 255))

# Defines sprites we'll use
#The c_ prefix denotes Fia's Hotpants Outfit
#The s_ prefix denotes Fia's Sweater Outfit
#The n_ prefix denotes Fia in the nude
#A 'w' in the prefix denotes a wet version
#The _u suffix denotes the fact Fia's tail is raised

#All the clothed sprites
image fia c_fire = "assets/sprites/fia_clothed_grin.png"
image fia c_neutral = "assets/sprites/fia_clothed_neutral.png"
image fia c_smile = "assets/sprites/fia_clothed_smile.png"
image fia c_pout = "assets/sprites/fia_clothed_pout.png"
image fia c_puppy = "assets/sprites/fia_clothed_sad.png"
image fia cw_pout = "assets/sprites/fia_clothedwet_pout.png"

#All the nude sprites
image fia n_smile = "assets/sprites/fia_nude_smile.png"  
image fia nw_smile = "assets/sprites/fia_nudewet_smile.png"

#All the sweater sprites
image fia s_bite = "assets/sprites/fia_sweater_lipbite.png"

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

init python:
    #Messes with the default dissolve
    define.move_transitions("dissolve",0.4)

# The acutal game starts here.
label start:
    #Start the VN with Fia & the MC outside
    scene black
    "..."
    "It's funny how quickly one loses track of time when you're sleeping under the sun."
    "Thirty minutes, an hour, three hours... I honestly can't say how long I've been here."
    "Not that that bothers me."
    "After all, Fia and I chose to stay in town over Spring Break for this very reason."
    "None of the usual hustle and bustle, none of the interruptions."
    "Just the two of us taking it easy and relaxing any way we can."
    "???" "...ike."
    "???" "MIKE."
    "Perhaps I spoke too soon about being able to relax..."
    
    #Open his eyes
    scene bg outside with circirisout
    #Anytime she changes sprites add "with dissolve"
    show fia c_pout with dissolve
    "As I open my eyes I'm greeted with the sight of my girlfriend looming over me."
    "I didn't even notice her leave my side under our tree."
    "There's plenty of good napping spots this far out in the hills, but we always come back to this one in particular."
    "I'm not entirely sure why we do at this point. Force of habit maybe?"
    "In any case, it seems Fia's tired of laying about."
    f "Jeez."
    f "I've been trying to wake you up for at least five minutes now!"
    "I let out a yawn and stretch before standing."
    mc "Did something come up?"
    show fia c_neutral with dissolve
    f "Maybe. Take a look over there."
    "She points over my shoulder at the sky behind us."
    "The normally crystal-blue horizon seems to be growing ever darker. An assemblage of clouds, thunderheads even."
    mc "Huh. I didn't think we were due for rain until tomorrow?"
    f "And we were having such a lovely time too..."
    "Her eyes shift downwards while her tail and ears droop."
    "It's understandable. One of her quirks is that she hates getting wet outside of showers and baths."
    "Those, for some reason, she absolutely adores."
    "Between that and the fact her current outfit is rather... susceptible to moisture and it's no wonder she's anxious."
    mc "Well I suppose we'd better head back then."
    f "Yeah..."
    show fia c_puppy with dissolve
    "And there it is. Her infamous \"kicked puppy\" look."
    "I know she's not doing it on purpose but it still makes me feel awful."
    "I should probably try and get her mind off of it."

    #First choice. Determines whether the MC opts for a tease or tries to be comforting
    menu:
        "Tease her a little":
            jump tease
        
        "Try to be comforting":
            jump comfort
            
    #We shouldn't ever get here but just in case...
    return

 #Scene used if the MC chooses to tease Fia
label tease:
    "The quickest way to get her to perk up might be to rib her a little."
    "A little tease there, a little sexual innuendo there..."
    mc "Well look on the bright side: At least now you have an excuse to pounce me when we get back."
    show fia c_neutral with dissolve
    f "Huh?"
    "I give her a wink."
    mc "I may have been out cold but I could still tell you were groping at my..."
    show fia c_pout with dissolve
    f "I did no such thing!"
    "And yet her tail is wagging. Seems I guessed right."
    mc "Uh huh. It's kinda hard to miss your paws, Fia."
    "She lets out a little whine in response. Curse her adorableness."
    f "Okay fine. I maybe sorta thought about waking you up in a different way."
    mc "Oh?"
    show fia c_fire with dissolve
    f "It involved forcing you up against the tree, tearing your clothes off, and..."
    "I wave her off before she gets too fired up. Mostly for the sake of my new shirt."
    mc "Alright alright, I get it. Let's getting walk though before you decide to change your mind and we get caught in the rain."
    "With that I start walking down the road back towards our apartment. Fia's quick to catch up."
    show fia c_smile with dissolve
    f "That's why you were playing possum, weren't you?"
    "It's my turn to be confused."
    mc "Eh?"
    f "You were secretly hoping I would wake you up like that~"
    "I let out a playful sigh. I walked right into that one."
    mc "You know how much I love it when you do."
    show fia c_fire with dissolve
    f "I'll have to do it more often then~"
    mc "I'm going to have to start wearing a chastity belt to bed, aren't I?"
    mc "Otherwise I'll never get any sleep."
    show fia c_smile with dissolve
    f "It wouldn't last five seconds."
    "She winks at me when I turn to raise an eyebrow at her."
    "It's her way of letting me know that if she's pushing too hard I can tell her."
    "But honestly?"
    "I don't mind in the slightest."
    "I'm just happy she's not dwelling on the storm gathering behind us."
    
    #Move to the Wet T-Shirt Scene
    jump wetshirt

label comfort: 
    "A little affection can go a long way. Especially with dogs."
    "Not that Fia is anything but a proud Hellhound, but that she shares some basic characteristics."
    "So I do what comes naturally: I reach out and pull her close into a hug."
    #Close up here? Need to figure out how to do that
    #If we do go with a close up it'll persist throughout this scene
    mc "Hey, Fia?"
    f "Yeah?"
    "I smile back as warmly as I can muster."
    mc "We can still cuddle when we get back home, you know."
    show fia c_smile with dissolve
    "A hint of a grin creeps across her face. A start, at least."
    f "I know..."
    f "It's just... it feels more special out here."
    "I give her a squeeze, which she promptly returns."
    mc "If I didn't know any better, I might think you're criticizing my cuddling abilities."
    "She lets out a sigh and pulls back."
    #If we did a close up, this is where we'd go back to normal
    show fia c_neutral with dissolve
    f "Mmm..."
    f "They could do with some improving."
    "Her deadpan tone might confuse anyone else, but not me."
    "As such, I match her tone."
    mc "You're right. Clearly the tree is the integral part of our cuddling equation."
    f "Exactly. Without the tree it means nothing at all."
    "I dramatically toss a hand over my face, as if in shame."
    mc "I suppose next you'll tell me that you want to bring other greenery into the bedroom..."
    f "Indeed. We clearly need to see other flora."
    "I turn back towards our tree, shaking my fist in mock rage."
    mc "Curse you and your damn mystical cuddling properties!"
    show fia c_smile with dissolve
    "It seems that is finally a bit too much for her to continue our humorous charade."
    "This time the grin that appears remains on her face."
    f "But really, you can't help but admire all that tree's done for us."
    "I nod, then start to walk beside her down along the road."
    "After all, there IS rain coming. We can't just sit here pillow-talking."
    "That can come later."
    mc "It's where we met, where we had our first kiss..."
    show fia c_fire with dissolve
    f "It's also where I jumped you for the first time~"
    "I let out a chuckle."
    mc "Maybe we really should bring the stupid thing with us."
    f "Nah. It'd get in the way of me smothering you with affection."
    mc "Only affection?"
    "She bites her lip, her intentions clear."
    f "Well I mean if you want me to spell it out in graphic detail..."

    #Move to the Wet T-Shirt Scene
    jump wetshirt

label wetshirt:
    #Thunder sound here?
    with vpunch
    "Before I can reply, though, a crack of thunder peels across the land."
    "Seconds later the windfront reaches us, carrying with it the first drops of rain."
    "It seems the storm was closer than either of us thought."
    show fia c_pout with dissolve
    f "Ugh. We're going to get soaking wet..."
    mc "Probably. But then again, you're always wet around me."
    "That earns me a playful punch on the shoulder."
    show fia c_smile with dissolve
    f "Come on, honey, we'd better hurry."
    
    #Need to make a rain overlay of sorts
    show fia cw_pout with dissolve
    f "Stupid rain!"
    jump apartment
    
label apartment:
    scene bg apartment with fade
    show fia cw_pout with dissolve
    f "I'm going to take a shower, you coming?"
    
    #Illusion of choice here. MC ends up in the shower either way
    menu:
        "Of course!":
            jump acceptance
        "Nah, you go ahead. I'll wait.":
            jump shower_foreplay

#Short scene as they get into the shower
label acceptance:
    show bg shower with fade
    show fia n_smile with dissolve
    f "Glad you decided to join me~"
    jump shower_sex

#Slightly longer scene as Fia strips the MC and "forces" him into the shower
label shower_foreplay:
    show bg shower with fade
    show fia n_fire with dissolve
    f "Yeah you're not getting away that easy~"
    jump shower_sex

#Soapy fun times followed by some slippery sex
label shower_sex:
    show fia nw_smile with dissolve
    f "Hurry up and write this so I can play with my bone!"
    jump post_shower

#After the shower scene
label post_shower:
    show fia s_bite with dissolve
    f "The sooner you write this the sooner I can love you tenderly in our fort~"
    return
