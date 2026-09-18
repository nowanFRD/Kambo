# Here's the code for the phone!

define nvl_mode = "classic"  ##Allow the NVL mode to become a phone conversation

init -1 python:
    phone_position_x = 0.3
    phone_position_y = 0.5

transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    xcenter pXalign
    yalign pYalign
    zoom 0.7

    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0

    
transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0

screen PhoneDialogue(dialogue, items=None):

    style_prefix "phoneFrame"
    frame at phone_transform(phone_position_x, phone_position_y), Transform(zoom=0.7):
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)
        viewport:
            draggable True
            mousewheel True
            # cols 1
            yinitial 1.0
            # scrollbars "vertical"
            vbox:
                null height 20
                use nvl_phonetext(dialogue)
                null height 100


screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        $ message_frame = "phone_received_frame.png"

        hbox:
            spacing 10
            
            #If this is the first message of the character, show an icon
            if previous_d_who != d.who:
                if d.who == name_fl:
                    $ message_icon = "phone_received_icon_fl.png"

                elif d.who == name_m:
                    $ message_icon = "phone_received_icon_m.png"
                    
                else:
                    $ message_icon = "phone_received_icon.png"

                add message_icon:
                    if d.current:
                        at message_appear_icon()
                    
            else:
                null width 107

            vbox:
                yalign 1.0
                if previous_d_who != d.who:
                    text d.who

                frame:
                    padding (20,20)
                    background Frame(message_frame, 23,23,23,23)
                    xsize 350

                    if d.current:
                        at message_appear(-1)

                    text d.what:
                        pos (0,0)
                        xsize 350
                        slow_cps False
                        color "#000"

                        id d.what_id
        $ previous_d_who = d.who
                    
style phoneFrame is default

style phoneFrame_frame:
    background Transform("phone_background.png", xcenter=0.5,yalign=0.5)
    foreground Transform("phone_foreground.png", xcenter=0.5,yalign=0.5)
    
    ysize 815
    xsize 495

style phoneFrame_viewport:
    yfill True
    xfill True

    yoffset -20

style phoneFrame_vbox:
    spacing 10
    xfill True