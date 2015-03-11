# Main script of the game
# Reference http://renpyhandbook.tumblr.com/code-tutorials as needed

#########################################
# Defines backgrounds we'll use
image bg outside = "assets/backgrounds/outside_bg.png"
image bg outside_rain = im.MatrixColor("assets/backgrounds/outside_bg.png", im.matrix.tint(0.7, 0.7, 0.7))
image bg shower = "assets/backgrounds/bathroom_bg.png"
image bg apartment = Placeholder("bg")
image black = Solid((0, 0, 0, 255))

#########################################
# Defines sprites we'll use
#The c_ prefix denotes Fia's Hotpants Outfit
#The s_ prefix denotes Fia's Sweater Outfit
#The n_ prefix denotes Fia in the nude
#A 'w' in the prefix denotes a wet version
#A 's' in the prefix denotes soap (Nude only, implies 'w')
#The _u suffix denotes the fact Fia's tail is raised (Default on Fire/Nude)

#All the clothed sprites
image fia c_fire = "assets/sprites/fia_clothed_grin.png"
image fia c_neutral = "assets/sprites/fia_clothed_neutral.png"
image fia c_smile = "assets/sprites/fia_clothed_smile.png"
image fia c_pout = "assets/sprites/fia_clothed_pout.png"
image fia c_puppy = "assets/sprites/fia_clothed_sad.png"
image fia cw_pout = "assets/sprites/fia_clothedwet_pout.png"
image fia cw_smile = Placeholder("girl")
image fia cw_fire = Placeholder("girl")
image fia cw_fire_smile = Placeholder("girl")

#All the nude sprites
image fia n_smile = "assets/sprites/fia_nude_smile.png"  
image fia n_fire = Placeholder("girl")
image fia nw_smile = "assets/sprites/fia_nudewet_smile.png"
image fia nw_fire = Placeholder("girl")
image fia nw_bite = Placeholder("girl")
image fia nws_smile = Placeholder("girl")

#All the sweater sprites
image fia s_bite = "assets/sprites/fia_sweater_lipbite.png"

#########################################
# Define the characters we'll use

#Unknown
define un = Character('???', what_prefix='"', what_suffix='"', show_two_window=True)

#Fia
define f = Character('Fia', color="#CC5252", what_prefix='"', what_suffix='"', show_two_window=True)

#The MC
#As his inner thoughts will be handled by the narrator we need to add quotes
define mc = Character("Mike", color="#F0FFFF", what_prefix='"', what_suffix='"', show_two_window=True)

#########################################
#Transitions and variables
init:
    $ circirisout = ImageDissolve("assets/backgrounds/circleiris.png", 1.5, 8)
    $ circirisin = ImageDissolve("assets/backgrounds/circleiris.png", 1.5, 8, reverse=True)
            
#init python:
    #Messes with the default dissolve
    #define.move_transitions("dissolve", 0.5)

#########################################
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
    un "MIKE."
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
    "Between that the obvious and it's no wonder she's anxious."
    mc "Well I suppose we'd better head back then."
    f "Yeah..."
    show fia c_puppy with dissolve
    "And there it is. Her infamous \"kicked puppy\" look."
    "I know she's not doing it on purpose but it still makes me feel awful."
    "I should probably try and get her mind off of it."

    #Removed dialogue choice. Just go to the next scene.
    jump tease
    
    #We should never get here, but just in case...
    return

#Scene where the MC teases Fia for being anxious about the rain
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
    "And yet your tail is wagging. Seems I guessed right."
    mc "Uh huh. It's kinda hard to miss your paws, Fia."
    "She lets out a little whine in response. Curse her adorableness."
    f "Okay fine. I maybe sorta thought about waking you up in a different way."
    mc "Oh?"
    show fia c_fire with dissolve
    f "It involved forcing you up against the tree, tearing your clothes off, and..."
    "I wave her off before she gets too fired up."
    mc "Alright alright, I get it. Let's getting walking before you decide to change your mind and we get caught in the rain."
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

#The obligatory wet t-shirt scene
label wetshirt:
    #Thunder sound here?
    with vpunch
    "Speaking of..."
    "A crack of thunder peels across the land, stopping me from replying."
    "Seconds later the windfront reaches us, carrying with it the first drops of rain."
    "It seems the storm was closer than either of us thought."
    show fia c_pout with dissolve
    f "Ugh. We're going to get soaking wet..."
    mc "Probably. But then again, you're always wet around me."
    "That earns me a playful punch on the shoulder."
    show fia c_smile with dissolve
    f "Come on, we'd better hurry."
    
    #Need to make a rain overlay of sorts
    scene bg outside_rain with dissolve
    "..."
    "It's times like this that make me consider always carrying an umbrella around."
    "Even my underwear is drenched. And not in the good way."
    "We're still a good mile and a half away from our apartment too."
    
    show fia cw_pout with dissolve
    "Not that I mind in the slightest."
    "Fia, on the other hand..."
    f "Grrrrr..."
    "I'm torn between wanting to laugh and to ogle her."
    "I know she doesn't mind the latter. Hell she encourages it normally."
    "The former, though, I should at least address. Even if it earns me another love tap."
    mc "You know, Fia..."
    f "What?"
    "She sounds absolutely dejected. I hope this works."
    mc "If I didn't know any better, I'd say you planned this whole thing from the start."
    "It takes her a moment to realize I'm talking about her outfit."
    show fia cw_smile with dissolve
    f "Not really. But it's a nice bonus, I guess?"
    mc "I'd say so."
    f "Too bad the effect doesn't work so well on your clothes, though."
    "I chuckle at that."
    mc "First the groping, now this... I'm starting to wonder if I'm just a piece of meat to you."
    "Again, it's all in good fun. And I make she knows for sure by winking."
    "It seems to have the intended effect as wisps of flames begin to seep from the corners of her eyes."
    "These aren't the flames of pure lust like from before, though."
    "These are ones of passion and adoration."
    show fia cw_fire with dissolve
    f "Never. But even if you were a literal steak I'd love you all the same."
    mc "Plus, if I were, you'd have more fun eating me."
    "She stops, dead in her tracks. I follow suit shortly thereafter."
    f "I don't think I'll ever get tired of devouring you, hun."
    mc "And I you, dear."
    "For a moment we just stare at each other in silence."
    "We're both trying not to laugh at our sappiness."
    "There's always so much sexual tension that sometimes we need moments like this for perspective."
    "Luckily for me, Fia cracks first."
    show fia cw_fire_smile with dissolve
    f "Maybe I should get caught in the rain more often~"
    "I can't resist reaching out and pulling her close."
    #zoom in
    "Both of our clothes makes a sort of squelching noise as the wet fabrics rub against each other."
    "Even through the chilling rain, I can feel Fia's swelling body heat as she presses against me."
    mc "I certainly wouldn't mind."
    "We look into each others eyes. Then, at the same time, our lips meet in midair."
    "It's a kiss of affection. Short, sweet, and just long enough to mean something."
    "Though, for all it matters, we could remain like this for hours. Rain and all."
    "Fia's the first to pull away."
    #zoom out
    show fia cw_fire with dissolve
    f "I hope you know what you've started~"
    "I let out a hearty laugh."
    mc "Of course I do. And I know you know I do because your hand wandered again."
    "It's true. My fly seems to be suspiciously down."
    show fia cw_pout with dissolve
    f "Oh I am SO going to tear into you when we get home."
    "I wink at her and start walking again."
    mc "We'd better stop flirting shamelessly and hurry then."
    show fia cw_smile with dissolve
    "As we plod onwards, Fia whispers something under her breath."
    "I don't quite catch all of it though."
    f "...so hard~"
    
    jump apartment

#MC & Fia enter the apartment. They quickly strip and hit the shower.
label apartment:
    scene bg apartment with fade
    "We arrive at our apartment some ten minutes later."
    "Seemingly just in time too, as the rain starts coming down even harder."
    
    show fia cw_smile with dissolve
    f "I guess it's a good thing we didn't do it out there."
    mc "Yeah, we'd probably be drowning right about now if we did."
    "She flashes a grin at me, then strips off her wet clothes."
    show fia nw_smile with dissolve
    f "Come on. Before we get too riled up let's at least try to wash up."
    "I follow her example and ditch my soggy, drenched coverings."
    "Now both nude, we both take a moment to drink the other in. Fia even bites her lip in anticipation."
    show fia nw_bite with dissolve
    mc "So about that shower..."
    f "Huh...?"
    "I repeat myself. Which is luckily all it takes to snap her out of it."
    show fia nw_fire with dissolve
    f "Oh, right. Come on, you~"
    "She turns deftly on her heels and starts leading the way to the bathroom."
    "All along the way she puts extra emphasis into her hip movements."
    "Even her tail gets into the seductive action: swishing side to side to accent her stride."
    "...have I mentioned how lucky I am yet?"
    
    scene bg shower with fade
    
    #Originally we had a choice here. But fuck that noise, Fia's switch has been flipped!  
    jump shower_sex


#Soapy fun times followed by some slippery sex
label shower_sex:
    show fia nws_smile with dissolve
    f "Hurry up and write this so I can play with my bone!"
    jump post_shower

#After the shower scene
label post_shower:
    show fia s_bite with dissolve
    f "The sooner you write this the sooner I can love you tenderly in our fort~"
    return
