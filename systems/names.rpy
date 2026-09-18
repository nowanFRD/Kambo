label pnc:
        
    default player_name = ""

    if _preferences.language == "english":
        $ player_name = renpy.input("What's his name?", length=12)

    elif _preferences.language == "japanese":
        $ player_name = renpy.input("{font=MPLUSRounded1c-Black.ttf}彼は何という名前ですか？{/font}", length=12)

    else:
        $ player_name = renpy.input("Как его зовут?", length=12)

    $ player_name = player_name.strip().capitalize()

    if not player_name:
        "Нет."
        jump pnc

    if " " in player_name:
        "Нет."
        jump pnc

    if not player_name.isalpha():
        "Нет."
        jump pnc

    if player_name in white_list_name:
        "Нет."
        jump pnc


    $ persistent.player = player_name

    jump fnc
        
label fnc:

    default flinn_name = ""

    if _preferences.language == "english":
        $ flinn_name = renpy.input("What's your friend's name?", length=12)

    elif _preferences.language == "japanese":
        $ flinn_name = renpy.input("{font=MPLUSRounded1c-Black.ttf}友達の名前は何ですか?{/font}", length=12)

    else:
        $ flinn_name = renpy.input("Как зовут вашего друга?", length=12)

    $ flinn_name = flinn_name.strip().capitalize()

    if not flinn_name:
        "Нет."
        jump fnc

    if " " in flinn_name:
        "Нет."
        jump fnc

    if not flinn_name.isalpha():
        "Нет."
        jump fnc
            
    if flinn_name in white_list_name:
        "Нет."
        jump fnc

    $ persistent.flinn = flinn_name
    
    jump enc

label enc:

    default eileen_name = ""

    if _preferences.language == "english":
        $ eileen_name = renpy.input("What's your sister's name?", length=12)

    elif _preferences.language == "japanese":
        $ eileen_name = renpy.input("{font=MPLUSRounded1c-Black.ttf}ご姉妹のお名前は何ですか？{/font}")

    else:        
        $ eileen_name = renpy.input("Как зовут вашу сестру?", length=12)

    $ eileen_name = eileen_name.strip().capitalize()

    if not eileen_name:
        "Нет."
        jump enc

    if " " in eileen_name:
        "Нет."
        jump enc

    if not eileen_name.isalpha():
        "Нет."
        jump enc

    if eileen_name in white_list_name:
        "Нет."
        jump enc

    $ persistent.eileen = eileen_name

    if persistent.playground_1 == True:
        call begining from _call_begining_1
    
    else:
        call epilogue from _call_epilogue_1