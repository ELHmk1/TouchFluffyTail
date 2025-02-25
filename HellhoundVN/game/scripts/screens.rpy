
##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=True):
    vbox:
        style "say_two_window_vbox"

        # if who:
        #     window:
        #         style "say_who_window"
        #
        #         text who:
        #             id "who"

        window:
            id "window"

            has vbox:
                style "say_vbox"

            text what id "what"
    if who:
        text who:
            id "who"
            yalign 0.93
            xpos 30

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    $ game_running = False

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
        add "images/gui/logo.png"
        text "[version]" color "#7C1919" xalign 0.99 yalign 0.99

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        ypos 110

        has vbox

        textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")
        #textbutton _("Credits") action Start("credits")
        #textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():
    window:
        style "gm_root"

    frame:
        #style_group "gm_nav"
        xalign .98
        ypos 110

        has vbox

        if game_running:
            textbutton _("Save Game") action ShowMenu("save")
        else:
            textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")
        if game_running:
            textbutton _("Main Menu") action MainMenu()
        #textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()
        textbutton _("Return") action Return()

screen mm_navigation():
    window:
        style "gm_root"

    frame:
        #style_group "gm_nav"
        xalign .98
        ypos 20

        has vbox

        #textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")
        #textbutton _("Main Menu") action MainMenu()
        #textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()
        textbutton _("Return") action Return()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"




##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker(operation):

    frame:

        #style "file_picker_frame"

        xpadding 50 ypadding 50
        xmargin 100 ymargin 50
        xsize 0.7

        has vbox

        label "{size=48}[operation]{/size}"
        null height 30

        # The buttons at the top allow the user to pick a
        # page of files.
        # hbox:
        #     style_group "file_picker_nav"
        #
        #     textbutton _("Previous"):
        #         action FilePagePrevious()
        #
        #     textbutton _("Auto"):
        #         action FilePage("auto")
        #
        #     textbutton _("Quick"):
        #         action FilePage("quick")
        #
        #     for i in range(1, 9):
        #         textbutton str(i):
        #             action FilePage(i)
        #
        #     textbutton _("Next"):
        #         action FilePageNext()

        $ columns = 2
        $ rows = 4

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            #xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    #xfill True
                    xsize 600

                    has hbox



                    # Add the screenshot.
                    add FileScreenshot(i)
                    null width 32
                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker("Save Game")

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker("Load Game")

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    text "[version]" color "#7C1919" xalign 0.99 yalign 0.99

    # Put the navigation columns in a three-wide grid.
    grid 2 1:
        xsize 0.65
        xalign 0.25
        yalign 0.5
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has hbox
                label _("Display")

                vbox:
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

            # frame:
            #     style_group "pref"
            #     has vbox
            #
            #     label _("Transitions")
            #     textbutton _("All") action Preference("transitions", "all")
            #     textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                vbox:
                    spacing 20

                    hbox:
                        xfill True
                        label _("Text Speed")
                        bar value Preference("text speed")

                    hbox:
                        xfill True
                        label _("Auto-Forward")
                        bar value Preference("auto-forward time")

                    if config.has_voice:
                        textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

            # frame:
            #     style_group "pref"
            #     has vbox
            #
            #     textbutton _("Joystick...") action Preference("joystick")

            frame:
                style_group "pref"
                has hbox

                label _("Skip")
                vbox:
                    textbutton _("Seen Messages") action Preference("skip", "seen")
                    textbutton _("All Messages") action Preference("skip", "all")

            # frame:
            #     style_group "pref"
            #     has vbox
            #
            #     textbutton _("Begin Skipping") action Skip()

        vbox:
            frame:
                style_group "pref"
                vbox:
                    spacing 20
                    hbox:
                        xfill True
                        label _("Music Volume")
                        bar value Preference("music volume")
                    hbox:
                        xfill True
                        label _("Sound Volume")
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test"):
                                action Play("sound", config.sample_sound)
                                style "soundtest_button"
            frame:
                style_group "pref"
                has hbox
                label _("Vignette Effect")

                vbox:
                    textbutton _("Enabled") action SetField(persistent, "vignette", True)
                    textbutton _("Disabled") action SetField(persistent, "vignette", False)

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

            frame:
                style_group "pref"
                has hbox
                label _("After Choices")
                vbox:
                    textbutton _("Stop Skipping") action Preference("after choices", "stop")
                    textbutton _("Keep Skipping") action Preference("after choices", "skip")

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
