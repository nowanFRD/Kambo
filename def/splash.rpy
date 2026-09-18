label splashscreen:

    if persistent.lang == True:
        $ quick_menu = False
        $ _game_menu_screen = None
        menu:
            "{font=MPLUSRounded1c-Black.ttf}Выберите язык / Select Language / 言語を選択{/font}"
        
            "Русский":
                $ renpy.change_language(None) 
            
            "English":
                $ renpy.change_language("english") 

            "{font=MPLUSRounded1c-Black.ttf}日本語{/font}":
                $ renpy.change_language("japanese")

    
    if _preferences.language == "japanese":
        show text "{font=MPLUSRounded1c-Black.ttf}本作品には性的嫌がらせ、暴力描写が含まれています。18歳未満の方のプレイは固く禁止されています。{/font}":
            zoom 1.0 alpha 1.0
            easein 3.0 zoom 1.5
            linear 1.0 alpha 0.0

    elif _preferences.language == "english":
        show text "The game contains sexual assault and violence; it is not allowed for underages":
            zoom 1.0 alpha 1.0
            easein 3.0 zoom 1.5
            linear 1.0 alpha 0.0


    else:
        show text "В игре присутствуют: Сексуальные домогательства, насилие, Запрещенно несовершеннолетним":
            zoom 1.0 alpha 1.0
            easein 3.0 zoom 1.5
            linear 1.0 alpha 0.0

    pause 4
    
    play music "audio/main_menu_music.ogg"
    show splash
    $ renpy.pause(4.0, hard=True)
    $ quick_menu = True
    $ _game_menu_screen = "save"
    return