label end:

    $ persistent.playground_1 = False

    $ persistent.playground_2 = True

    $ quick_menu = False

    $ _game_menu_screen = None

    scene black with dissolve    

    if _preferences.language == "japanese":

        show text "{color=#fff}{font=PixelMPlus10-Regular.ttf}{size=50}おわり...？{/size}{/font}{/color}" at truecenter with slow_dissolve
    
    elif _preferences.language == "english":
        show text "{color=#fff}{font=ArcadeJeu-Regular.otf}{size=50}End?{/size}{/font}{/color}" at truecenter with slow_dissolve

    else:
        show text "{color=#fff}{font=ArcadeJeu-Regular.otf}{size=50}Конец...?{/size}{/font}{/color}" at truecenter with slow_dissolve
    
    pause 3
    
    hide text with dissolve

    pause 5
    
    if _preferences.language == "japanese":
        show text "{color=#fff}{font=PixelMPlus10-Regular.ttf}{size=50}二年後{/size}{/font}{/color}" at truecenter with slow_dissolve
    
    elif _preferences.language == "english":
        show text "{color=#fff}{font=ArcadeJeu-Regular.otf}{size=50}Two years ago.{/size}{/font}{/color}" at truecenter with slow_dissolve

    else:
        show text "{color=#fff}{font=ArcadeJeu-Regular.otf}{size=50}Два года спустя.{/size}{/font}{/color}" at truecenter with slow_dissolve

    hide text with dissolve

    pause 3

    call start from _call_start

label end1:
    
    $ persistent.playground_1 = True

    $ persistent.playground_2 = False

    $ quick_menu = False

    $ _game_menu_screen = None

    scene black with dissolve

    play music kazoku

    show credits
    
    $ renpy.pause(60.0, hard=True)

    hide credits

    pause 3

    stop music 

    if _preferences.language == "japanese":
        show text "{color=#fff}{font=MPLUSRounded1c-Black.ttf}{size=50}履歴を完了しました。永続的なデータは削除されます。{/size}{/font}{/color}" at truecenter with slow_dissolve
    
    elif _preferences.language == "english":
        show text "{color=#fff}{size=50}You have completed the story. Persistents will be deleted soon.{/size}{/color}" at truecenter with slow_dissolve

    else:
        show text "{color=#fff}{size=50}Ты прошел историю. Постоянные данные будут удалены.{/size}{/color}" at truecenter with slow_dissolve

    call screen clickable_up_text_end

    $ renpy.pause(0.5, hard=True)

    hide text with dissolve

    pause 3

    $ creations = creating()
    
    $ persistent._clear()
    
    $ renpy.quit()