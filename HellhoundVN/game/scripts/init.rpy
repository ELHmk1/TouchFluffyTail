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

image fia neutral = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="neutral", brows="neutral", mouth="neutral", ears="up", tail="down", blush="", flames=False)
image fia worried = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="neutral", brows="middleup", mouth="neutral", ears="up", tail="down", blush="", flames=False)
image fia smile = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="squint", brows="raised", mouth="smile", ears="up", tail="up", blush="light", flames=False)
image fia pout = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="squint", brows="middleup", mouth="pout", ears="down", tail="down", blush="light", flames=False)
image fia grin fire = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="squint2", brows="raised2", mouth="widegrin", ears="up", tail="up", blush="strong", flames=True)
image fia smile fire = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="squint2", brows="raised2", mouth="smile", ears="up", tail="up", blush="strong", flames=True)
image fia bite fire = DynamicDisplayable(draw_clothing, character=fia, art_path="images/sprites/fia/", eyes="halfopen", brows="raised", mouth="lipbite", ears="up", tail="up", blush="strong", flames=True)


define un = Character('???', what_prefix='"', what_suffix='"', show_two_window=True)

#Fia
define f = Character('Fia', color="#B72743", image="fia", what_prefix='"', what_suffix='"', show_two_window=True)

#The MC
#As his inner thoughts will be handled by the narrator we need to add quotes
define mc = Character("Mike", color="#E0D6CD", what_prefix='"', what_suffix='"', show_two_window=True)
#NVL mode narrator
define mc_nvl = Character(None, kind=nvl, ctc="ctc_blink", ctc_position="nestled")


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
    narrator = Character(None, window_left_padding=160)
    fia = Actor()

    state = "dry"


    sportsbra = Clothing("white_sportsbra", priority=10, wettable=True, barbie=True)
    shirt = Clothing("shirt", priority=10, wettable=True, barbie=True)
    hotpants = Clothing("hotpants", priority=10, wettable=True)
    shorts = Clothing("shorts", priority=10, wettable=True)
    sweater = Clothing("sweater", priority=10, wettable=True)

    fia.wear(sportsbra)
    fia.wear(shorts)

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
