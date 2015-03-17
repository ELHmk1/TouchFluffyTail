# Main script of the game
# Reference http://renpyhandbook.tumblr.com/code-tutorials as needed

#########################################
# Defines backgrounds we'll use
image bg outside = "assets/backgrounds/outside_bg.png"
image bg outside_rain = im.MatrixColor("assets/backgrounds/outside_bg.png", im.matrix.tint(0.7, 0.7, 0.7))
image bg shower = "assets/backgrounds/bathroom_bg.png"
image bg apartment = Placeholder("bg")
image black = Solid((0, 0, 0, 255))
image insert_cg1 = "assets/CGs/insert_cg1.png"

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
image fia cw_pout = "assets/sprites/fia_clothedwet_pout.png"
image fia cw_neutral = Placeholder("girl")
image fia cw_smile = Placeholder("girl")
image fia cw_fire = Placeholder("girl")
image fia cw_fire_smile = Placeholder("girl")

#All the nude sprites
image fia n_smile = "assets/sprites/fia_nude_smile.png"  
image fia n_fire = Placeholder("girl")
image fia n_neutral = Placeholder("girl")
image fia nw_smile = "assets/sprites/fia_nudewet_smile.png"
image fia nw_fire = Placeholder("girl")
image fia nw_bite = Placeholder("girl")
image fia nw_neutral = Placeholder("girl")
image fia nws_smile = "assets/sprites/fia_nude_soap_smile.png"
image fia nws_fire = Placeholder("girl")

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
#NVL mode narrator
define mc_nvl = Character(None, kind=nvl, ctc="ctc_blink", ctc_position="nestled")

#########################################
#Transitions, variables, and what not
init:
    $ circirisout = ImageDissolve("assets/backgrounds/circleiris.png", 1.5, 8)
    $ circirisin = ImageDissolve("assets/backgrounds/circleiris.png", 1.5, 8, reverse=True)
    
    image rain:
        "assets/backgrounds/rain.png"
        0.2
        "assets/backgrounds/rain2.png"
        0.2
        "assets/backgrounds/rain3.png"
        0.2
        repeat
        
    image ctc_blink:
        "assets/sprites/ctc01.png"
        linear 0.5 alpha 1.0
        "assets/sprites/ctc03.png"
        linear 0.5 alpha 1.0
        repeat

init python:
    #NVL stuff
    menu = nvl_menu

    # The color of a menu choice when it isn't hovered.
    style.nvl_menu_choice.idle_color = "#ccccccff"

    # The color of a menu choice when it is hovered.
    style.nvl_menu_choice.hover_color = "#ffffffff"

    # The color of the background of a menu choice, when it isn't
    # hovered.
    style.nvl_menu_choice_button.idle_background = "#00000000"

    # The color of the background of a menu choice, when it is
    # hovered.
    style.nvl_menu_choice_button.hover_background = "#ff000044"

    # How far from the left menu choices should be indented.
    style.nvl_menu_choice_button.left_margin = 20

    
    #style.nvl_window.background = "nvl_window.png"
    style.nvl_window.xpadding = 55
    style.nvl_window.ypadding = 305

    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    
    #Messes with the default dissolve
    define.move_transitions("dissolve", 0.4)

#########################################
# The acutal game starts here.
label start:
    #Start the VN with the MC resting
    scene black with fade
    window show
    mc_nvl "..."
    mc_nvl "It's funny how quickly one loses track of time when you're sleeping under the afternoon sun."
    mc_nvl "Thirty minutes, an hour, three hours... I honestly can't say how long I've been here."
    mc_nvl "Not that that bothers me."
    mc_nvl "After all, Fia and I just finished a rather long hike."
    mc_nvl "She wanted to get a certain snapshot for her work, something about the lighting."
    mc_nvl "Naturally I went with her."
    mc_nvl "Some six hours later and we'd only just made it back to the outskirts of roads more familiar."
    mc_nvl "She might be able to go that long without rest, but not me."
    window hide
    nvl clear
    un "Mike~"
    "Please no."
    un "Mike."
    "No. I don't want to get up."
    un "MIKE."
    "...no rest for the wicked, I suppose."
    
    #Open his eyes
    scene bg outside 
    show fia c_pout
    with circirisout
    "As I open my eyes I'm greeted with the sight of my girlfriend looming over me."
    "I didn't even notice her leave my side under the tree we'd stopped at to rest."
    f "Jeez."
    f "I've been trying to wake you for at least five minutes now!"
    "I let out a yawn and stretch before standing."
    "There's even an audible pop as my shoulder rotates."
    mc "Not everyone can go as long as you do, Fia."
    show fia c_neutral with dissolve
    f "Well if you'd come with me more often, maybe you'd have better endurance."
    "Ah."
    mc "You know how it is. The spirit is willing..."
    show fia c_smile with dissolve
    f "Are you going to be alright though? I don't mind waiting a little longer."
    show fia c_fire with dissolve
    f "Nor would I mind carrying you."
    "The dull ache in my feet makes her offer sorely tempting."
    "But I can't wimp out now. Not after doing so well!"
    mc "How are you going to carry the camera bag if your arms are full of me?"
    "She takes the bag without complaint. Well, aside from a mocking pout."
    show fia c_pout with dissolve
    f "At this rate I'm going to be the one wearing the pants in this relationship."
    mc "Well you can't have mine."
    "We both chuckle at that one."
    show fia c_fire with dissolve
    f "Oh I don't know. I think we both know my feelings about that."
    "The way her gaze drifts down and lingers makes me realize she's not just flirting with me."
    "I follow her stare, only to realize my fly is suspiciously down."
    mc "Huh."
    "I quickly rectify the displaced zipper."
    mc "I thought I dreamt that part."
    f "Nope~"
    f "I was THIS close to waking you up in a different way."
    mc "Oh?"
    f "It involved forcing you up against the tree, tearing your clothes off, and..."
    "I wave her off before she gets too fired up."
    mc "Alright alright, I get it. Let's getting walking again before you decide to change your mind."
    "With that I start walking down the road back towards our apartment. Fia's quick to catch up."
    show fia c_smile with dissolve
    f "That's why you were playing possum, weren't you?"
    "I turn to look at her, confused."
    mc "Eh?"
    f "You were secretly hoping I would wake you up like that."
    "I let out a playful sigh. I walked right into that one."
    mc "You know how much I love it when you do."
    show fia c_fire with dissolve
    f "I'll have to do it more often then."
    "I don't know whether to be happy or sad for my pelvis."
    mc "I'm going to have to start wearing a chastity belt to bed, aren't I?"
    mc "Otherwise I'll never get any sleep."
    show fia c_smile with dissolve
    f "It wouldn't last five seconds."
    "This time when she winks, she smiles sweetly."
    "It's her way of letting me know that if she's pushing too hard I can tell her."
    "She's not, but I can't afford to let her get me worked up out here."
    "Especially since the afternoon forecast DID call for some form of rain."
    "Oh... well there's an idea."
    "Fia hates getting wet outside of showers and baths."
    "Those, for some reason, she absolutely adores."
    mc "Hey, Fia."
    show fia c_neutral with dissolve
    f "Hm?"
    mc "You do remember that we're due for rain later, right?"
    f "Yeah... what about it?"
    mc "Well if we keep flirting like this, we'll never make it back to the apartment in time."
    show fia c_pout with dissolve
    "It doesn't take her long to see right through me to the real problem."
    f "I can easily make THAT more managable, right now, if you'd let me."
    "I shake my head in response."
    mc "You know how I am. The thought of being watched terrifies me."
    "Her mouth opens and closes twice wordlessly. Then her features soften."
    show fia c_neutral with dissolve
    f "It just occurred to me that we've never talked about that sort of thing before."
    mc "Huh?"
    "She re-slings her camera bag and walks out in front of me. Once there she spins around and walks backwards."
    f "Like... I know you're not into the whole exhibitionism thing. But terrified? That's new."
    f "I thought it was just that it didn't do anything for you."
    "I scratch the back of my head in thought."
    mc "I think it's way too much risk for the reward the thrill brings you."
    mc "Not that the thrill is at all bad, just that there are consequences if you get caught."
    "Fia giggles at that."
    show fia c_smile with dissolve 
    f "I suppose that's true."
    f "Well... kinda."
    f "In this day in age that sort of thing is becoming less and less taboo, you know?"
    "I shrug noncommittally."
    mc "Maybe. But I'd still prefer not to be judged. By accident or otherwise."
    f "Awww~ Does this means I have to stop secretly rating your performance?"
    "Another sigh escapes my lips. This is going to be a long walk home."
    
    #Onto the next scene!
    jump wetshirt
    
    #We should never get here, but just in case...
    return

#The obligatory wet t-shirt scene
label wetshirt:
    hide fia
    window show
    mc_nvl "We spend the next ten or so minutes walking in silence."
    mc_nvl "Along the way, Fia returns to walking at my side."
    mc_nvl "Much closer than before I might add."
    mc_nvl "So close, in fact, that I can't help feel the occasional tingle as her fur brushes against my skin."
    mc_nvl "I have to visibly concentrate on keeping a straight face. Which just makes Fia all the more radiant."
    mc_nvl "Sadly, it seems my stoic front is short lived..."
    window hide
    nvl clear
    
    #Thunder sound here?
    with vpunch
    "A crack of thunder peels across the land, stopping me from replying."
    "Seconds later a windfront reaches us, carrying with it the first drops of rain."
    "It seems the forecasted storm was closer than either of us thought."
    "That or we took far longer walking back than expected."
    "...yeah it's probably the latter."
    f "Ugh. We're going to get soaking wet..."
    show fia c_pout with dissolve
    "I look to my right to see a rather disgruntled-looking Hellhound."
    mc "Told you we should have brought along an umbrella."
    f "It'dve just been something else to carry though!"
    mc "Maybe. We might have been able to stuff it in your bag there."
    mc "I wouldn't be surprised if you could see specks of dirt on the surface of Mars with all that gear."
    show fia c_neutral with dissolve
    f "Well with the right lenses..."
    "She mulls this over, a thoughtful expression on her face."
    f "Best I can get you is the Moon."
    "I'm honestly impressed at that."
    "Though the rain hits us proper before I can respond."
    
    scene bg outside_rain
    show rain 
    with dissolve
    window show
    mc_nvl "The next few minutes are a whirl of us sputtering and trying to make a makeshift covering."
    mc_nvl "It doesn't go so well."
    mc_nvl "Even my underwear ends up drenched. And not in the good way."
    mc_nvl "As we're still a good mile and a half away from our apartment, we're resigned to walking home drenched."
    window hide
    nvl clear
    show fia cw_pout with dissolve
    "Not that I mind in the slightest."
    "Fia, on the other hand..."
    f "Grrrrr..."
    "I'm torn between wanting to laugh and to ogle her."
    mc "You know, Fia..."
    f "What?"
    mc "If I didn't know any better, I'd say you planned this whole thing from the start."
    "It takes her a moment to realize I'm talking about her outfit."
    show fia cw_smile with dissolve
    "As a result, she gives me a playful shove. Just enough to send me momentarily off balance."
    f "Honestly, I just wanted to get that creek done before it was too late."
    mc "The lighting or something again?"
    show fia cw_neutral with dissolve
    "She nods. As she does, little droplets trail from her head, only to be lost in the downpour."
    f "Yeah. Starting next week the sun won't be at the right angle."
    f "Plus, with all this rain, the water level would be too high."
    mc "You've put a lot of thought into this, haven't you?"
    "Another nod."
    show fia cw_smile with dissolve
    f "A lot of people just think it's about pointing your camera in the right direction at the right time."
    f "But you also have to take into consideration the exposure length, aperture size, and so on."
    f "And for every one good photo I take there's at least fifty or so that are awful."
    "Even with the semi-blinding rain, I pick up on the fact she's got a new spring in her step."
    "It's great seeing her like this. And I don't just mean the obvious."
    "Seeing and hearing about something she's passionate about seems special, in a way."
    mc "I guess I'm just surprised, since you don't actually ever submit the photographs themselves."
    "It's true. She uses them exclusively as references for her painting and other art."
    "You wouldn't think a Hellhound could paint with paws and claws like those, let alone take photos."
    "But her work often speaks for itself."
    f "I like keeping things fresh in my mind."
    f "That or it can be handy when I come back to something later and wonder what I was working towards."
    f "Which... come to think of it..."
    show fia cw_fire with dissolve
    "Uh oh. I know that look."
    f "I seem to recall working on something not too long ago..."
    "And I was doing so well..."
    "Maybe if I play it cool I'll buy myself some time."
    mc "I..."
    "Of course, as I open my mouth to speak, she steps right in front of me and stops."
    "I all but slam into her as a result."
    #zoom in?
    "Both of our clothes make a sort of squelching noise as the wet fabrics rub against each other."
    "Even through the chilling rain, I can feel Fia's swelling body heat as she presses against me."
    "As I look into her eyes, she opens her mouth ever so slightly and tilts her head."
    "..."
    "Damn it I can't resist it any longer."
    "I take her by the shoulders, then force our lips together."
    "It's a kiss of lust and affection. Short, sweet, and just long enough to mean something."
    "Enough to drive her wild and relent. Or so I hope."
    "As it turns out, Fia's the first to pull away."
    #zoom out
    f "I hope you know what you've started~"
    "I let out a hearty laugh."
    mc "Of course I do. And I know you know I do because your hand wandered again."
    "It's true. My fly seems to be down once more."
    show fia cw_pout with dissolve
    f "Oh I am SO going to tear into you when we get home."
    "I wink at her and start walking again."
    "As we plod onwards, Fia whispers something under her breath."
    "I don't quite catch all of it though."
    show fia cw_smile with dissolve
    f "...so hard~"
    
    jump apartment

#MC & Fia enter the apartment. They quickly strip and hit the shower.
label apartment:
    scene bg apartment with fade
    "We finally arrive at our apartment some ten minutes later."
    "Seemingly just in time too, as the rain starts coming down even harder."
    show fia cw_smile with dissolve
    f "I guess it's a good thing we didn't do it out there."
    mc "Yeah, we'd probably be drowning right about now if we did."
    "She flashes a grin at me, then sets her bag aside."
    "Her clothes vanish as it they're nothing, tossed aside into a pile by the laundry room door."
    show fia nw_smile with dissolve
    f "Come on. Before we get too riled up let's at least try to wash up."
    "I follow her example and start to ditch my soggy, drenched coverings."
    "As I do, I can't help but comment on something."
    mc "It is kinda odd though, washing up just to get dirty all over again."
    "She snickers at that, eyes drinking me in as I continue to strip."
    f "It's a different kind of dirty though. A good kind."
    "I shoot her a enthusiastic grin."
    mc "No argument there."
    "I finishly shortly thereafter. Not because I was deliberately stalling but because I was trying not to lose my balance."
    "Now both nude, we both take a moment to stare at each other."
    "Fia's first to crack, biting her lip in anticipation."
    show fia nw_bite with dissolve
    "From what I know about her, she's about two seconds away from tackling me when she looks like that."
    "Though I think I can push her just a little more."
    mc "So about that shower..."
    f "Huh...?"
    "I repeat myself. Which is luckily all it takes to snap her out of it."
    show fia nw_fire with dissolve
    f "Oh, right. Come on, you~"
    "She turns deftly on her heels and starts leading the way to the bathroom."
    "All along the way she puts extra emphasis into her hip movements."
    "Even her tail gets into the seductive action: swishing side to side to accent her stride."
    "As arousing as the action is, I can't help but notice one thing."
    "Each flick is sending beads of water splattering against the wall and me"
    "Either she doesn't notice or doesn't care. Perhaps I should follow suit and focus on what's important."
    "...Not that that's hard."
    
    scene bg shower with fade
    "Once we reach the bathroom Fia wastes no time."
    "She hops into the glass enclosure and starts up the hot water."
    "Soon steam fills the room, and with it a welcome heat."
    #show steam
    show fia nw_smile
    with dissolve
    "The moisture also comes with a moan as the water washes over her."
    f "Ahhhhhh~ Much much better..."
    "After tossing her hair out of her eyes, she turns to beckon at me with a finger."
    f "Well just don't stand there!"
    mc "Just wanted to give you a second or two."
    "We're pretty fortunate in that we have a pretty large bathroom."
    "Otherwise there'd never be enough room for us to take a shower together like this."
    "...though it's not like we're anything but close right now."
    "And since I'm right next to her I can see where all this steam is coming from."
    "About half of the water that hits her fur seems to be instantly turning to vapor."
    "Although I've seen it before I have to admit, it's a pretty neat way to keep her coat clean."
    "Though it does leave her ashen skin rather vulnerable."
    mc "Pass the soap, would you?"
    f "Soap, right..."
    "Even over the sound of the rushing water I can hear her short, excited breaths echoing across the tiles."
    "She's so close to breaking. Evidenced further when she bends over and purposely flaunts herself to me."
    f "Cinammon or Apple scented?"
    "Don't stare at it."
    "Don't stare..." 
    "...and I'm looking at it."
    mc "Uh... cherry."
    "She giggles and slowly stands up right with a bottle in hand."
    f "We don't have cherry. But let's just go with apple."
    show fia nws_smile with dissolve
    window show
    mc_nvl "Somehow we manage to get halfway through rubbing each other down."
    mc_nvl "Which, given the circumstances, seems like a miniature miracle."
    mc_nvl "Each new inch I slide my hands over causes her to pry at my own skin and groan in delight."
    mc_nvl "But our restraint finally breaks when we start on each other's chests."
    window hide
    nvl clear
    f "Mhn~"
    f "That's it. Rub it in nice and slow~"
    "Dutifully I continue my work. Starting with the undersides of her breasts."
    "From there my hands move upwards, coming to cup them before applying a squeeze."
    mc "Like this?"
    "I don't even wait for a reply before letting my thumbs slip over her areola."
    show fia nws_fire with dissolve
    f "Ah! Yes~"
    "Her claws, currently on my chest, dig into my skin as a result. Not enough to be unpleasantly painful though."
    "I repeat the process once more for good measure."
    "Though this time, it's enough to break Fia."
    f "Hnn... I can't take it anymore~"
    "She whirls on the spot and throws herself against the glass door while lifting her ass."
    f "Get inside me this instant."
    f "And don't you dare stop until the water goes cold."
    
    #Onto the actual sex scene!
    jump shower_sex

#Actual sex scene
label shower_sex:
    scene insert_cg1 with fade
    pause
    f "Hurry up and write this!"
    jump post_shower

#After the shower scene
label post_shower:
    show fia s_bite with dissolve
    f "The sooner you write this the sooner I can love you tenderly in the bedroom~"
    return
