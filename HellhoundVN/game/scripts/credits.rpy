#Handles the Credits Screen

#Actual stuff
label credits:
    scene black
    $ credits_speed = 25 #scrolling speed in seconds
    show cred at Move((0.5, 2.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    return
    
init python:
    credits= ('Art', 'Monorus'), ('Writing', 'ELH'), ('Editing & Proofing', 'RSAnon')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.99.0.303"
    
init:
    image black = Placeholder("bg")
    image cred = Text(credits_s, font="assets/playtime.ttf", color="#FFFFFF", text_align=0.5)
    image theend = Text("{color=#ffffff}{size=80}The end{/size}{/color}", xalign=0.5, yalign=0.5)
    
