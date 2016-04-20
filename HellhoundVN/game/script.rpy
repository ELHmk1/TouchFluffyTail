# Main script of the game
# Reference http://renpyhandbook.tumblr.com/code-tutorials as needed

#########################################
# Defines backgrounds we'll use
image bg apartment = Placeholder("bg")
image bg bedroom = Placeholder("bg")
image black = Solid((0, 0, 0, 255))
image insert_cg1 = "images/CGs/insert_cg1.png"

#########################################
# Defines sprites we'll use
#The c_ prefix denotes Fia's Hotpants Outfit
#The s_ prefix denotes Fia's Sweater Outfit
#The n_ prefix denotes Fia in the nude
#A 'w' in the prefix denotes a wet version
#A 's' in the prefix denotes soap (Nude only, implies 'w')
#The _u suffix denotes the fact Fia's tail is raised (Default on Fire/Nude)


image fia neutral = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="neutral", brows="neutral", mouth="neutral", ears="up", tail="down", blush="", flames=False)
image fia worried = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="neutral", brows="middleup", mouth="neutral", ears="up", tail="down", blush="", flames=False)
image fia smile = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="squint", brows="raised", mouth="smile", ears="up", tail="up", blush="light", flames=False)
image fia pout = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="squint", brows="middleup", mouth="pout", ears="down", tail="down", blush="light", flames=False)
image fia grin fire = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="squint2", brows="raised2", mouth="widegrin", ears="up", tail="up", blush="strong", flames=True)
image fia smile fire = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="squint2", brows="raised2", mouth="smile", ears="up", tail="up", blush="strong", flames=True)
image fia bite fire = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="halfopen", brows="raised", mouth="lipbite", ears="up", tail="up", blush="strong", flames=True)

#########################################
# Define the characters we'll use

#Unknown
define un = Character('???', what_prefix='"', what_suffix='"', show_two_window=True)

#Fia
define f = Character('Fia', color="#CC5252", image="fia", what_prefix='"', what_suffix='"', show_two_window=True)

#The MC
#As his inner thoughts will be handled by the narrator we need to add quotes
define mc = Character("Mike", color="#F0FFFF", what_prefix='"', what_suffix='"', show_two_window=True)
#NVL mode narrator
define mc_nvl = Character(None, kind=nvl, ctc="ctc_blink", ctc_position="nestled")

#########################################
#Transitions, variables, and what not
init:
    define dis = Dissolve(0.2)

    $ circirisout = ImageDissolve("images/backgrounds/circleiris.png", 1.5, 8)
    $ circirisin = ImageDissolve("images/backgrounds/circleiris.png", 1.5, 8, reverse=True)

    image rain:
        "images/backgrounds/rain.png"
        0.033334
        "images/backgrounds/rain2.png"
        0.033334
        "images/backgrounds/rain3.png"
        0.033334
        "images/backgrounds/rain4.png"
        0.033334
        "images/backgrounds/rain5.png"
        0.033334
        "images/backgrounds/rain6.png"
        0.033334

        "images/backgrounds/rain4.png"
        0.033334
        "images/backgrounds/rain2.png"
        0.033334
        "images/backgrounds/rain.png"
        0.033334
        "images/backgrounds/rain4.png"
        0.033334
        "images/backgrounds/rain3.png"
        0.033334
        "images/backgrounds/rain6.png"
        0.033334
        repeat
    
    #Click to continue indicator
    image ctc_blink:
        "images/sprites/ctc01.png"
        linear 0.5 alpha 1.0
        "images/sprites/ctc03.png"
        linear 0.5 alpha 1.0
        repeat
    
    #Defines the Vignette toggle for later 
    if persistent.vignette is None:
        $ persistent.vignette = True
    
    #Defines the flash effect for use during climaxes
    $ flash = Fade(.25, 0, .75, color="#fff")

init python:
    fia = Actor()

    state = "dry"

    shirt = Clothing("shirt", priority=10, wettable=True, barbie=True)
    hotpants = Clothing("hotpants", priority=10, wettable=True)
    sweater = Clothing("sweater", priority=10, wettable=True)

    fia.wear(shirt)
    fia.wear(hotpants)

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
    style.nvl_window.xpadding = 215
    style.nvl_window.ypadding = 305

    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    
    #Messes with the default dissolve
    #define.move_transitions("dissolve", 0.2)
    

#########################################
# The acutal game starts here.
label start:

label intro:
    #Start the VN with the MC resting
    scene black with fade
    centered "Keep in mind this is a teaser."
    centered "Names, sprites, etc. may change in the finished product."
    "..."
    "It's funny how quickly one loses track of time when you're sleeping under the afternoon sun."
    "Thirty minutes, an hour, three hours... I honestly can't say how long I've been here."
    "Not that that bothers me."
    "After all, Fia and I just finished a rather long hike."
    "She wanted to get a certain snapshot for her work, something about the lighting."
    "Naturally I went with her."
    "Some six hours later and we'd only just made it back to the outskirts of roads more familiar."
    "She might be able to go that long without rest, but not me."
    un "Mike~"
    "Please no."
    un "Mike."
    "No. I don't want to get up."
    un "MIKE."
    "...no rest for the wicked, I suppose."
    
    #Open his eyes
    scene bg outside 
    show fia pout
    with circirisout
    "As I open my eyes I'm greeted with the sight of my girlfriend looming over me."
    "I didn't even notice her leave my side under the tree we'd stopped at to rest."
    f "Jeez."
    f "I've been trying to wake you for at least five minutes now!"
    "I let out a yawn and stretch before standing."
    "There's even an audible pop as my shoulder rotates."
    mc "Not everyone can go as long as you do, Fia."
    show fia neutral with dis
    f "Well if you'd come with me more often, maybe you'd have better endurance."
    "Ah."
    mc "You know how it is. The spirit is willing..."
    show fia smile with dis
    f "Are you going to be alright though? I don't mind waiting a little longer."
    show fia grin fire with dis
    f "Nor would I mind carrying you."
    "The dull ache in my feet makes her offer sorely tempting."
    "But I can't wimp out now. Not after doing so well!"
    mc "How are you going to carry the camera bag if your arms are full of me?"
    "She takes the bag without complaint. Well, aside from a mocking pout."
    show fia pout with dis
    f "At this rate I'm going to be the one wearing the pants in this relationship."
    mc "Well you can't have mine."
    "We both chuckle at that one."
    show fia grin fire with dis
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
    show fia smile with dis
    f "That's why you were playing possum, weren't you?"
    "I turn to look at her, confused."
    mc "Eh?"
    f "You were secretly hoping I would wake you up like that."
    "I let out a playful sigh. I walked right into that one."
    mc "You know how much I love it when you do."
    show fia grin fire with dis
    f "I'll have to do it more often then."
    "I don't know whether to be happy or sad for my pelvis."
    mc "I'm going to have to start wearing a chastity belt to bed, aren't I?"
    mc "Otherwise I'll never get any sleep."
    show fia smile with dis
    f "It wouldn't last five seconds."
    "This time when she winks, she smiles sweetly."
    "It's her way of letting me know that if she's pushing too hard I can tell her."
    "She's not, but I can't afford to let her get me worked up out here."
    "Especially since the afternoon forecast DID call for some form of rain."
    "Oh... well there's an idea."
    "Fia hates getting wet outside of showers and baths."
    "Those, for some reason, she absolutely adores."
    mc "Hey, Fia."
    show fia neutral with dis
    f "Hm?"
    mc "You do remember that we're due for rain later, right?"
    f "Yeah... what about it?"
    mc "Well if we keep flirting like this, we'll never make it back to the apartment in time."
    show fia pout with dis
    "It doesn't take her long to see right through me to the real problem."
    f "I can easily make THAT more manageable, right now, if you'd let me."
    "I shake my head in response."
    mc "You know how I am. The thought of being watched terrifies me."
    "Her mouth opens and closes twice wordlessly. Then her features soften."
    show fia neutral with dis
    f "It just occurred to me that we've never talked about that sort of thing before."
    mc "Huh?"
    "She re-slings her camera bag and walks out in front of me. Once there she spins around and walks backwards."
    f "Like... I know you're not into the whole exhibitionism thing. But terrified? That's new."
    f "I thought it was just that it didn't do anything for you."
    "I scratch the back of my head in thought."
    mc "I think it's way too much risk for the reward the thrill brings you."
    mc "Not that the thrill is at all bad, just that there are consequences if you get caught."
    "Fia giggles at that."
    show fia smile with dis 
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
    "We spend the next ten or so minutes walking in silence."
    "Along the way, Fia returns to walking at my side."
    "Much closer than before I might add."
    "So close, in fact, that I can't help feel the occasional tingle as her fur brushes against my skin."
    "I have to visibly concentrate on keeping a straight face. Which just makes Fia all the more radiant."
    "Sadly, it seems my stoic front is going to be rather short lived..."
    
    #Thunder sound here?
    with vpunch
    "A crack of thunder peels across the land."
    "Seconds later a windfront reaches us, carrying with it the first drops of rain."
    "It seems the forecasted storm was closer than either of us thought."
    "That or we took far longer walking back than expected."
    "...yeah it's probably the latter."
    f "Ugh. We're going to get soaking wet..."
    show fia pout zorder 0 with dis
    "I look to my right to see a rather disgruntled-looking Hellhound."
    mc "Told you we should have brought along an umbrella."
    f "It'dve just been something else to carry though!"
    mc "Maybe. We might have been able to stuff it in your bag there."
    mc "I wouldn't be surprised if you could see specks of dirt on the surface of Mars with all that gear."
    show fia neutral with dis
    f "Well with the right lenses..."
    "She mulls this over, a thoughtful expression on her face."
    f "Best I can get you is the Moon."
    "I'm honestly impressed at that."
    "Though the rain hits us proper before I can respond."
    
    show rain zorder 1 with Dissolve(2.0)
    "The next few minutes are a whirl of us sputtering and trying to make a makeshift covering."
    show bg outside rain with Dissolve(2.0)
    "It doesn't go so well."
    "Even my underwear ends up soaked. And not in the good way."
    $ state = "dripping"
    show fia worried with dis
    "As we're still a good mile and a half away from our apartment, we're resigned to walking home drenched."
    show fia pout with dis 
    "Not that I mind in the slightest."
    "Fia, on the other hand..."
    f "Grrrrr..."
    "I'm torn between wanting to laugh and to ogle her."
    mc "You know, Fia..."
    f "What?"
    mc "If I didn't know any better, I'd say you planned this whole thing from the start."
    "It takes her a moment to realize I'm talking about her outfit."
    show fia smile with dis
    "As a result, she gives me a playful shove. Just enough to send me momentarily off balance."
    f "Honestly, I just wanted to get that creek done before it was too late."
    mc "The lighting or something again?"
    show fia neutral with dis
    "She nods. As she does, little droplets trail from her head only to be lost in the downpour."
    f "Yeah. Starting next week the sun won't be at the right angle."
    f "Plus, with all this rain, the water level would be too high."
    mc "You've put a lot of thought into this, haven't you?"
    "Another nod."
    show fia smile with dis
    f "A lot of people just think it's about pointing your camera in the right direction at the right time."
    f "But you also have to take into consideration the exposure length, aperture size, and so on."
    f "And for every one good photo I take there's at least fifty or so that are awful."
    "Even with the semi-blinding rain, I pick up on the fact she's got a new spring in her step."
    "It's great seeing her like this. And I don't just mean the obvious."
    "Seeing and hearing about something she's passionate about seems special, in a way."
    mc "I guess I'm just surprised, since you don't actually ever submit the photographs themselves."
    "It's true. She uses them exclusively as references for her paintings and other art, or so I've observed."
    "You wouldn't think a Hellhound could paint with paws and claws like those, let alone take photos."
    "But her work often speaks for itself."
    f "Well they're also like little memory windows."
    f "I can pick up any photograph and tell you who I was with, what I was thinking, and so on."
    f "Inspiration's a tricky thing. Even the smallest detail could lead to breakthrough."
    "She pauses, then adds in an afterthought,"
    f "They can also be a good pick-me-up when I'm feeling down."
    mc "Huh."
    mc "I never knew they meant that much to you."
    "A nod."
    f "I know it must seem a little weird."
    mc "Not at all."
    mc "Though if that's the case, why don't you have many photos of you and I together?"
    "It's an innocent question. I honestly don't mind either way."
    "I never could stand couples who felt the need to plaster themselves on every surface."
    show fia pout with dis
    f "Mostly because neither of us is very photogenic."
    mc "Could have fooled me."
    f "You know what I mean!"
    f "I haven't yet been able to capture US properly."
    "She trails off, blushing just a tad redder as she does."
    "As a result we spend the next couple of minutes walking in silence once more."
    show fia neutral with dis
    f "Does it bother you though?"
    mc "Not really."
    f "Hmmm..."
    "She stares at me unblinking for a few seconds, even through the downpour."
    show fia grin fire with dis
    f "Well, if it's any consolation, I do have a TON of mental photographs of you."
    "Uh oh. I know that look."
    f "Though most of them ARE of you in rather... compromising situations."
    "And I was doing so well..."
    "Maybe if I play it cool I'll buy myself some time."
    mc "I..."
    "Of course, as I open my mouth to speak, she steps right in front of me and stops."
    "I all but slam into her as a result."
    #zoom in?
    #show fia cw_kiss with dis
    "Both of our clothes make a sort of squelching noise as the wet fabrics rub against each other."
    "Despite the chilling rain I can feel Fia's swelling body heat as she presses against me."
    "As I look into her eyes, she opens her mouth ever so slightly and tilts her head."
    "..."
    "Damn it I can't resist it any longer."
    "I take her by the shoulders, then force our lips together."
    "It's a kiss of lust and affection. Short, sweet, and just long enough to mean something."
    "Enough to drive her wild and relent. Or so I hope."
    "As it turns out, Fia's the first to pull away."
    #zoom out
    show fia grin fire with dis
    f "I hope you know what you've started~"
    "I let out a hearty laugh."
    mc "Of course I do. And I know you know I do because your hand wandered again."
    "It's true. My fly seems to be down once more."
    show fia pout with dis
    f "Oh I am SO going to tear into you when we get home."
    "I wink at her and start walking again."
    "As we plod onwards, Fia whispers something under her breath."
    "I don't quite catch all of it though."
    show fia smile with dis
    f "...so hard~"
    
    jump apartment

#MC & Fia enter the apartment. They quickly strip and hit the shower.
label apartment:
    $ state = "wet"
    scene bg apartment with fade
    "We finally arrive at our apartment some ten minutes later."
    "Seemingly just in time too, as the rain starts coming down even harder."
    show fia smile with dis
    f "I guess it's a good thing we didn't do it out there."
    mc "Yeah, we'd probably be drowning right about now if we did."
    "She flashes a grin at me, then sets her bag aside."
    "Her clothes vanish as it they're nothing, tossed aside into a pile by the laundry room door."
    $ fia.remove(shirt)
    show fia smile with dis
    $ fia.remove(hotpants)
    show fia smile with dis
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
    show fia bite fire with dis
    "From what I know about her, she's about two seconds away from tackling me when she looks like that."
    "Though I think I can push her just a little more."
    mc "So about that shower..."
    f "Huh...?"
    "I repeat myself. Which is luckily all it takes to snap her out of it."
    show fia grin fire with dis
    f "Oh, right. Come on, you."
    "She turns deftly on her heels and starts leading the way to the bathroom."
    "All along the way she puts extra emphasis into her hip movements."
    "Even her tail gets into the seductive action: swishing side to side to accent her stride."
    "As arousing as the action is I can't help but notice one thing."
    "Each flick is sending beads of water splattering against the wall and me"
    "Either she doesn't notice or doesn't care. Perhaps I should follow suit and focus on what's important."
    "...Not that that's hard."
    
    scene bg shower with fade
    "Once we reach the bathroom Fia wastes no time."
    "She hops into the glass enclosure and starts up the hot water."
    "Soon steam fills the room, and with it a welcome heat."
    $ state = "dripping"
    #show steam
    show fia smile with dis
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
    "Though it does leave her skin rather vulnerable."
    mc "Pass the soap, would you?"
    f "Soap, right..."
    "Even over the sound of the rushing water I can hear her short, excited breaths echoing across the tiles."
    "She's likely close to breaking. Evidenced when she bends over and purposely flaunts herself to me."
    f "Cinnamon or Apple scented?"
    "Don't stare at it."
    "Don't stare..." 
    "...and I'm looking at it."
    mc "Uh... cherry."
    "She giggles and slowly stands up right with a bottle in hand."
    f "We don't have cherry. But let's just go with apple."
    show fia smile with dis
    "Somehow we manage to get halfway through rubbing each other down."
    "Which, given the circumstances, seems like a miniature miracle."
    "Each new inch I slide my hands over causes her ashen skin to erupt in goosebumps of pleasure."
    "It's not before she starts to pry at my own skin and groan in delight."
    "It's become a game: who will snap first?"
    "That answer's short in coming when we start on each other's chests."
    f "Mhn~"
    f "That's it. Rub it in nice and slow~"
    "Dutifully I continue my work. Starting with the undersides of her breasts."
    "From there my hands move upwards, coming to cup them both before squeezing gently."
    mc "Like this?"
    "I don't even wait for a reply before letting my thumbs slip over her areola."
    "Immediately she twitches and lets out a whine."
    show fia grin fire with dis
    f "Ah! Yes~"
    "Her claws, currently on my chest, dig into me as well. Not enough to be unpleasantly painful though."
    "I repeat the process once more for good measure."
    "This time it's enough to break Fia."
    f "Hnn... I can't take it anymore..."
    "She whirls on the spot and throws herself against the glass door."
    "All the while she lifts up her tail to give me free access to both of her holes."
    f "You. In me. NOW."
    f "And don't you DARE stop until the water goes cold."
    
    #Onto the actual sex scene!
    jump shower_sex

#Actual sex scene
label shower_sex:
    scene ev shower1 with fade
    pause
    "The words are hardly out of her mouth before I move into place behind her."
    "Between the steam, running water, and her own juices, Fia's a sopping mess."
    "Which just makes sliding into her trivial."
    f "Mhn~!"
    "As her molten folds envelop me I feel them begin to grip and pull at my length."
    "It's as if the fires of hell itself are trying to burn the very essence of ecstasy into my flesh."
    "By the time I've hilted myself my entire pelvic region is awash in delight."
    "But perhaps the most arousing thing for me is how Fia reacts."
    "Her entire body tensed when I first entered but now she feels like putty in my hands."
    "What was once her gasps is now actual pants."
    "Between that and the way her tail instinctively coils around my waist I'm left throbbing with desire inside of her."
    f "Don't move... just yet..."
    mc "You just came, didn't you?"
    "Her interior clamps down around my base, holding me in place and preventing me from going anywhere."
    "Not that I was planning on it."
    f "Yeah... I guess I was really worked up, huh?"
    "She turns and gives me an embarrassed smile."
    "It's rare that she lets me take the lead like this, so seeing that just makes it all the more sensual."
    "I find myself beaming back at her, both proud and somehow more turned on than when we started."
    mc "For what it's worth, I already feel like I could go at any second too."
    f "Well don't hold back. Take it slow if you must but I WILL be draining those balls."
    f "One way or another."
    "As if to punctuate her statement, waves of pressure begin cascading down from my tip."
    "Her clamp on me relaxes at the same time."
    "I start slow, basing my thrusting pace on the subtle way her tail pulls at me with each cycle."
    "The wet fur feels luxurious, like a silken glove tickling across my skin."
    "With each completed motion its pulls grow hungrier and hungrier in nature."
    "Soon I'm not so sure whether it's my hips or her tail doing the work."
    "At some point, the showerhead starts spewing nothing but steam."
    "Or, rather, the water instantly evaporates the second it touches Fia."
    "With it comes the distinct smell of baked apple spice pie thanks to the soap she'd picked out."
    "All that combined with the way her folds keep drawing me back in with teasing licks of flame quickly bring me to the edge."
    mc "Fia I'm..."
    f "Inside. Do it inside!"
    "Her pleading is all it takes for me to topple over the knife's edge."
    "As I thrust my hips forward she bucks back into them."
    "There again she locks me in place and assaults my length with a barrage of burning nips."
    #White flash? (use 'with flash')
    "So powerful is my release that my entire body starts twitching involuntarily."
    "I can feel my seed flow into her, mixing with her juices and somehow igniting them."
    "The inferno drags my orgasm out, each rapturous moment echoing throughout my body with explosive intensity that makes my toes curl."
    "I couldn't tell you exactly how long she kept me in that state." 
    "It's only when I start to fall backwards, weak at the knees, that she relents."
    "Eyes full of love, lust, and concern, she holds me in place and waits."
    f "Breathe, Mike. That's a good boy."
    "It takes me a moment to collect myself."
    "All the while my own pantings mix with hers."
    mc "That... That was only the beginning, wasn't it?"
    "Her grin increases and she gives me a squeeze down below."
    "The swirling hellfire reignites about my length, allowing me to I quickly recover."
    f "Of course it was. But I won't take as much this time."
    mc "How considerate of you."
    "We both snicker at that before returning to the business at hand."
    "After she lets me go we quickly fall back into a pattern."
    "I start off in the lead but shortly end up being led by her."
    "The illusion of control, but a welcome one."
    "I end up losing track of how many times either of us cums."
    "The only real indicator of it is the mixture of liquids seeping out of Fia's slot."
    "It dribbles down her inner thighs to the reflective tile floor below."
    f "So much... Ah... For the shower..."
    mc "I wouldn't... worry..."
    "Somehow our pace increases. By now I'm all but jackhammering her against the door."
    "It's hard to say which is louder: her moans and whines, the reverberating glass, or my own grunts."
    "We only just catch ourselves in time when the glass begins to crack."
    f "Damn... Damn it... We just fixed that!"
    mc "Good thing we keep spares around, huh?"
    f "Yeah..."
    "We come to a complete stop as a result."
    "Though Fia slyly teases one more spasm from me before she lets me go."
    
    scene bg shower with fade
    #Did we want to do cum versions?
    show fia grin fire with dis
    "As soon as I stop convulsing inside of her I slide out, take a few steps back, and collapse against the opposite wall." 
    "With a giggle, Fia reaches between her legs and scrapes some of the cum mixture up in a claw."
    "She brings it to her eyes and considers it for a moment."
    "Then she makes a show of using her tongue to clean the digit."
    f "Mmmmmm~ The pineapple diet's DEFINITELY working."
    mc "That's... good..."
    "To say I'm winded would be an understatement."
    "My entire body feels like it just ran a marathon through the depths of hell itself."
    "I know she wants to keep going though."
    "While matching her stamina may be out of my reach, I still want to try."
    "Not out of some vain need to prove myself. More that I just don't want to let Fia down."
    mc "I just need a minute here. Yeah... a minute..."
    "The torrent of flames emanating from Fia's eyes die down to about half of their original size."
    show fia smile with dis
    f "You need more than that. I know. But it's cute that you're trying."
    "Damn her keen senses."
    "She joins me on the floor and stays next to me as the shower returns to normal."
    f "Take all the time you need, Mike."
    mc "Thanks."
    "Once our breathing returns to something semi-normal she proceeds to actually wash the pair of us."
    "It's not nearly as heated as before. If anything her touch is gentle and tender."
    "The only betrayal of her arousal is how she lingers on my pelvic region."
    "That she doesn't finish until she's given me several teasing pumps with her paws."
    f "And stand... careful now..."
    "She dunks us under the stream of liquid coming from the shower head. By now it's just started to lose its warmth."
    "Once all the traces of soap have disappeared from our bodies she turns off the water and begins drying us off."
    "By which, of course, I mean her body heat momentarily soars and leaves us with but a few droplets here and there."
    show fia smile with dis
    "Again the heavy scent of spiced apples fills the room."
    f "There we are. Come on. Let's go lay down."
    jump post_shower

#After the shower scene
label post_shower:
    scene bg bedroom with fade
    show fia smile with dis
    $ state = "dry"
    "It's a quick walk from the bathroom to the bedroom."
    "Once there, we both fall onto the sheets and curl up facing one another."
    f "You okay?"
    "She squeezes my shoulder lovingly."
    mc "Fine. Just winded. Really winded."
    f "We really are going to have to work on your endurance."
    f "But for now?"
    "Suddenly her lips press against mine for a quick peck."
    f "I'm more than content with that."
    f "You've come a long way from the adorably nervous guy I hounded way back when."
    "I flash her a grin at that."
    mc "Well... Thanks."
    mc "For not pressuring me or going too far. It makes me feel safe and comfortable, you know?"
    "A pauses follows my poorly constructed outcry of emotions."
    "Then I hear something thumping heavily against the mattress behind Fia."
    f "You have no idea how happy hearing that makes me."
    "This time I'm the one who kisses her."
    mc "I can guess."
    "I flip over and snuggle against her."
    "Now the little spoon, her arms instinctively wrap around me and pull me even closer."
    "As she does another peel of thunder and lightning erupts outside."
    
    show fia neutral with dis
    f "Jeez. It's still coming down pretty hard out there, isn't it?"
    mc "Seems so. Good thing we didn't have anything planned this weekend."
    "I hear a sigh. Then Fia buries her face into my nape."
    f "I really do need to paint at some point. And we both have exams in a couple of weeks to study for."
    f "But I'm sorely tempted just to ignore all that."
    mc "I can't imagine what for."
    "She squeezes the wind out of me. Just for a moment."
    f "Honestly it's a wonder I get anything productive done around you."
    mc "I could say the same, really."
    "I feel myself being turned over. Right into her waiting lips."
    f "Although..."
    show fia smile with dis
    f "Don't think you're entirely off the hook."
    mc "Huh?"
    "She spins me back over and then lets one of her paws drift downwards."
    f "I plan on a little breakfast in bed tomorrow morning~"
    "Oh boy..."
    scene bg black with circirisin
    
    #For now that's the end. If we expand to day 2 then we'll jump here
    jump credits
    return
