#Colors & Effects
image smoke = "images/smoke.png"
image vignette_effect = "images/vignette.png"
image white = "#ffffff"
image red = "#8B0000"
image blue = "#00008B"
image green = "#046307"
#Audios
define audio.water = "audio/sfx/water.ogg"
define audio.kiss = "audio/sfx/kiss.ogg"
define audio.eileen_scream = "audio/sfx/eileen_scream.ogg"
define audio.screamer = "audio/sfx/screamer.ogg"
define audio.alarm = "audio/sfx/alarm.ogg"
define audio.shoot = "audio/sfx/pistol-shoot.ogg"
define audio.airport = "audio/sfx/airplane.ogg"
define audio.kazoku = "audio/music/ex6.ogg"
define audio.miracle_of_crowbar = "audio/music/ex.ogg" 
define audio.idk = "audio/music/ex1.ogg" 
define audio.deepcare = "audio/music/ex2.ogg" 
define audio.forever = "audio/music/ex3.ogg" 
define audio.phone = "audio/sfx/phone_sound.ogg" 
define audio.bell = "audio/sfx/bell.ogg" 
define audio.housebell = "audio/sfx/housebell.ogg"
define audio.door_closed = "audio/sfx/door_closed.ogg"
define audio.crashing_door = "audio/sfx/crashing_door.ogg"
define audio.kambo_mood = "audio/music/ex4.ogg"
define audio.fall = "audio/sfx/fall.ogg"
define audio.smash = "audio/sfx/smash.ogg"
define audio.smashing = "audio/sfx/smashing.ogg" 
define audio.shock = "audio/sfx/shock.ogg"
#constants
define gui.textbox_background = Frame(Solid("#000000a8"), borders=Borders(2, 2, 2, 2))
define gui.namebox_background = Frame(Solid("#ffffffa8"), borders=Borders(1, 1, 1, 1))
define white_list_name = ["Камбо", "камбо","Kambo", "kambo", "Молли", "молли", "Molli", "molli", "Эйлин", "эйлин", "Eileen", "eileen"]
#defaults
default creations = ""
default end_choise = False
default system_name = ""
default asleep = False
default deal = False
default deal_2 = False
default ex1 = False
default ex2 = False
default ex3 = False
default no_listen = False
default kiss = False
default kiss1 = False
default name_o = _("Старец")
default name_mo = _("Мама")
default name_m = _("Маша")
default name_c = _("Камбо")
default name_f = _("Отец")
default name_me = _("Мама Эйлин")
default name_t = _("Таксист")
default name_mol = _("Молли")
default name_fl = _("Флинн")
default name_med = _("Врач")
default name_p = _("Павел")
default name_a = _("Алексей")
#Mov
image credits = Movie(play="images/mov/credits.webm")
image facetoface = Movie(play="images/Molli/facetoface.webm", loop=True)
image colt = "images/kambo/colt.png"
image main_menu = Movie(play="gui/main_menu.webm", loop=True)
image splash = Movie(play="images/mov/splash.webm")
image confession = Movie(play="images/Molli/confession.webm", loop=True)
#Backgrounds
image bg beach = "images/bg/new/beach.png"
image bg miami = "images/bg/new/miami.png"
image bg room4 = "images/bg/new/miami_room.png"
image bg room3 = "images/bg/new/miami_room.png"
image bg bel_harbor = "images/bg/new/bel_harbor.png"
image bg riviera_bich = "images/bg/new/riviera_bich.png"
image bg airport = "images/bg/new/airport.png"
image bg elektrostal = "images/bg/new/elektro.png"
image bg balkon_night = "images/bg/new/balcony_at_night.png"
image bg balkon = "images/bg/new/balcony.png"
image bg kitchen_miami = "images/bg/new/miami_kitchen.png"
image bg palata2 = "images/kambo/palata2.png"
image bg palata = "images/bg/palata.png"
image bg alexey_home_inside = "images/bg/ah.png"
image bg taxi2 = "images/bg/car1.png"
image bg alexey_home = "images/bg/a.png"
image bg pavel_home = "images/bg/ph.png"
image bg pavel_room = "images/bg/p.png"
image bg molli_house = "images/bg/new/Apartment_Exterior.png"
image bg village = "images/bg/village.png"
image bg room = "images/bg/room.png"
image bg kitchen = "images/bg/kitchen.png" 
image bg katcheli = "images/bg/katcheli.png"
image bg okraine = "images/bg/okraine.png"
image bg school = "images/bg/school.png"
image bg classroom = "images/bg/classroom.png"
image bg fhouse = "images/bg/fhouse.png"
image bg fhouse1 = "images/bg/fhouse1.png"
image bg fambar = "images/bg/fambar.png"
image bg fbasement = "images/bg/fbasement.png"
image bg masha_room = "images/bg/masha_room.png"
image bg hosp1 = "images/bg/GBUZ-MO.png"
image bg hospital = "images/bg/hospital.png"
image bg car = "images/bg/car.png"
image bg pavel_car = "images/bg/pavel_car.png"
image bg room2 = "images/bg/room2.png"
image bg kitchen2 = "images/bg/kitchen2.png"
image bg fire = "images/bg/fire.png"
image bg pavel_car1 = "images/bg/pavel_car1.png"
image txs ground = "images/textures/ground.png"
#Chr
define c_nvl = Character("[name_c]", kind=nvl)
define m_nvl = Character("[name_m]", kind=nvl)
define fl_nvl = Character("[name_fl]", kind=nvl)
define o = Character("[name_o]", color="#FFFFFF")
define mo = Character("[name_mo]", color="#FFFFFF")
define m = Character("[name_m]", color="#FFFFFF")
define c = Character("[name_c]", color="#FFFFFF")
define f = Character("[name_f]", color="#FFFFFF")
define t = Character("[name_t]", color="#FFFFFF")
define mol = Character("[name_mol]", color="#FFFFFF") 
define fl = Character("[name_fl]", color="#FFFFFF")
define med = Character("[name_med]", color="#FFFFFF")
define p = Character("[name_p]", color="#FFFFFF")
define a = Character("[name_a]", color="#FFFFFF")


image Error = "images/Error.png"
image Error1 = "images/Error1.png"

image test:
    "images/test.jpg"
    fit "contain"
    xysize (497, 702)
image test1:
    "images/test1.jpg"
    fit "contain"
    xysize (497, 702)
image test2:
    "images/test2.jpg"
    fit "contain"
    xysize (497, 702)
image test3:
    "images/test3.jpg"
    fit "contain"
    xysize (497, 702)
image test4:
    "images/test4.jpg"
    fit "contain"
    xysize (497, 702)
image test5:
    "images/test5.jpg"
    fit "contain"
    xysize (497, 702)