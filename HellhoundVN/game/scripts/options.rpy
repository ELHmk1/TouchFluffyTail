init -2 python:
    version = "v0.1-pre"

init -1 python hide:
    config.developer = True

    config.screen_width = 1920
    config.screen_height = 1080
    config.framerate = 60

    config.window_title = u"Hellhound VN - %s" %version

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "Hellhound VN"
    config.version = version

    #########################################
    # Themes

    ## We then want to call a theme function. theme.roundrect is
    ## a theme that features the use of rounded rectangles.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.glow(
        ## Theme: Glow
        ## Color scheme: Colorblind

        ## The color of an idle widget face.
        widget = "#898989",

        ## The color of a focused widget face.
        widget_hover = "#464646",

        ## The color of the text in a widget.
        widget_text = "#CCCCCC",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#6D5450",

        ## The color of a disabled widget face.
        disabled = "#898989",

        ## The color of disabled widget text.
        disabled_text = "#1C1B1B",

        ## The color of informational labels.
        label = "#190E16",

        ## The color of a frame containing widgets.
        frame = "#231E1F",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        # mm_root = "#261F1E",
        mm_root = "images/backgrounds/title.png",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        # gm_root = "#261F1E",
        gm_root = "images/backgrounds/title_blur.png",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    # style.window.background = Frame("frame.png", 12, 12)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 35
    style.window.right_padding = 35
    style.window.top_padding = 15
    style.window.bottom_padding = 0

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 155


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.
    # Mess with this later
    style.default.font = "fonts/tcceb.ttf"

    ## The default size of text.
    style.default.size = 32

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to True if the game has voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    # config.main_menu_music = "main_menu_theme.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.
    config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = None

    ## Used between screens of the game menu.
    config.intra_transition = None

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = None

    ## Used when returning to the main menu from the game.
    config.game_main_transition = None

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = None

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = None

    ## Used when a game is loaded.
    config.after_load_transition = None

    ## Used when the window is shown.
    config.window_show_transition = None

    ## Used when the window is hidden.
    config.window_hide_transition = None

    ## Used when showing NVL-mode text directly after ADV-mode text.
    config.adv_nvl_transition = dissolve

    ## Used when showing ADV-mode text directly after NVL-mode text.
    config.nvl_adv_transition = dissolve

    ## Used when yesno is shown.
    config.enter_yesno_transition = None

    ## Used when the yesno is hidden.
    config.exit_yesno_transition = None

    ## Used when entering a replay
    config.enter_replay_transition = None

    ## Used when exiting a replay
    config.exit_replay_transition = None

    ## Used when the image is changed by a say statement with image attributes.
    config.say_attribute_transition = None

    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persistent information can be found by the init code.)
python early:
    config.save_directory = "HellhoundVN-1423813676"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    #config.enter_transition = dissolve
    #config.exit_transition = dissolve
    #config.intra_transition = dissolve
    #config.main_game_transition = dissolve
    #config.game_main_transition = dissolve
    #config.end_splash_transition = dissolve
    #config.end_game_transition = dissolve
    #config.after_load_transition = dissolve
    #config.window_show_transition = dissolve
    #config.window_hide_transition = dissolve

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 0

    ## The default auto-forward time setting.

    config.default_afm_time = 10

    #########################################

    style.hyperlink_text.color = "#912330"
    style.hyperlink_text.hover_color = "#BA6236"


    style.slider.left_bar = Frame("images/gui/bar_full.png", 30, 40)
    style.slider.right_bar = Frame("images/gui/bar_empty.png", 30, 40)
    style.slider.hover_left_bar = Frame("images/gui/bar_hover.png", 30, 40)
    style.slider.thumb = None
    style.slider.thumb_offset = 0
    style.slider.ysize = 75
    style.slider.xsize = 300
    style.slider.left_gutter = 7
    style.slider.right_gutter = 7

    style.pref_slider.xsize = 300
    #style.pref_slider.xanchor= 1.0


    style.frame.background = Frame("images/gui/frame.png", 48, 48)
    style.frame.xpadding = 35
    style.frame.ypadding = 30

    style.label_text.size = 36
    style.label_text.color = "#4C3531"

    style.pref_button_text.size = 36
    style.pref_button.yminimum = 105
    style.pref_button.xminimum = 300

    style.window.background = Image("images/gui/dialogue_box.png")
    style.window.top_padding = 32
    #style.window.yalign = 1.0

    #style.say_who_window.xalign = 0.0
    #style.say_who_window.yalign = 1.0
    #style.say_who_window.left_padding = 15
    #style.say_who_window.top_padding = 15
    #style.say_who_window.right_padding = 15
    #style.say_who_window.bottom_padding = 15
    #style.say_who_window.xminimum = 150
    #style.say_who_window.yminimum = 15
    #style.say_who_window.xfill = False
    style.say_who_window.background = None
    style.say_who_window.yoffset = 50

    #style.say_label.drop_shadow = [(1, 1)]
    #style.say_label.drop_shadow_color = "#000000"
    style.say_label.size = 42
    #style.say_label.text_align = 0.5
    #style.say_label.xalign = 0.5
    style.say_label.font = "fonts/playtime.ttf"

    style.say_dialogue.font = "fonts/playtime.ttf"
    style.say_dialogue.size = 42
    style.say_window.left_padding = 160
    style.say_dialogue.color = "#E0D6CD"



    style.button.insensitive_background = Frame("images/gui/button_ground.png", left=32, top=24, right= 32, bottom=48)
    style.button.background = Frame("images/gui/button_idle.png", left=32, top=24, right= 32, bottom=48)
    style.button.hover_background = Frame("images/gui/button_hover.png", left=32, top=24, right= 32, bottom=48)
    style.button.selected_background = Frame("images/gui/button_selected_idle.png", left=32, top=24, right= 32, bottom=48)
    style.button.selected_hover_background = Frame("images/gui/button_selected_hover.png", left=32, top=24, right= 32, bottom=48)


    style.button.yminimum = 115
    style.button.xminimum = 300
    style.button.selected_top_padding = 15

    style.button.focus_mask = Image("images/gui/button_focus_mask.png")

    style.button.bottom_padding = 32
    style.button.xpadding = 32

    style.button_text.size = 46
    style.button_text.color = "#190E16"
    style.button_text.hover_color = "#28101A"
    style.button_text.selected_color = "#633431"
    style.button_text.selected_hover_color = "#7D423E"

    style.mm_button.insensitive_background = Frame("images/gui/button_ground.png", left=32, top=24, right= 32, bottom=48)

    style.file_picker_button.idle_background = Frame("images/gui/button_idle.png", left=32, top=24, right= 32, bottom=48)
    style.file_picker_button.insensitive_background = Frame("images/gui/button_ground.png", left=32, top=24, right= 32, bottom=48)
    style.file_picker_button.hover_background = Frame("images/gui/button_hover.png", left=32, top=24, right= 32, bottom=48)
    #style.file_picker_button.selected_background = Frame("images/gui/button_selected_idle.png", left=32, top=24, right= 32, bottom=48)
    #style.file_picker_button.selected_hover_background = Frame("images/gui/button_selected_hover.png", left=32, top=24, right= 32, bottom=48)

    style.file_picker_button.xpadding = 41
    style.file_picker_button.top_padding = 24
    style.file_picker_button.bottom_padding = 48

    style.file_picker_text.size = 32
    style.file_picker_text.color = "#190E16"
    style.file_picker_text.hover_color = "#28101A"
    #style.file_picker_text.selected_color = "#633431"
    #style.file_picker_text.selected_hover_color = "#7D423E"
    style.file_picker_text.insensitive_color = "#1F1C1C"


    ## Adjust screenshot size for save slots
    config.thumbnail_width = 230
    config.thumbnail_height = 129

    style.quick_button_text.size = 24

    #style.button_text.outlines = [(2, "#f76e60", 0, 0)]
    #style.button_text.outlines = (2, "#f76e60", 0, 0)

    # Vignette effect

    # This allows for the effect to be toggled
    def vignette_overlay():
        if persistent.vignette:
            ui.image("images/backgrounds/vignette.png")

    #We have to move the text layer up now too
    config.layers = ['master', 'overlay', 'text', 'transient', 'screens', ]
    config.say_layer="text"
    config.overlay_functions.append(vignette_overlay)
