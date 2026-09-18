init python:
    import os
    import getpass
    import math
    import platform

    def get_os_username():
        try:
            return getpass.getuser()
        except Exception:
            return os.environ.get("USER") or os.environ.get("USERNAME") or "Игрок"

    os_name = platform.system()

    renpy.music.register_channel("sech", loop=True)

    def creating():
        with open(fpath, "w", encoding="utf-8") as file:
            file.write("Hi dear player. I was really glad you finished this. I must be greatful and i am. If you reading this you should know that, i really be glad to see your feedback on itch.io, or via my tg @daoedyo. If you make me know you enjoy this then, i eventually make a siquels. Also i don't take money from you but if you want you can give a gift in telegram, this'll make me happy by the way.")

    fpath = os.path.join(config.gamedir, "thanks.txt")
    