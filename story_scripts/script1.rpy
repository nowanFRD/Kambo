label start:
    stop music fadeout 1
    $ system_name = get_os_username()
    if persistent.lang == True:
        call pnc from _call_pnc
    elif persistent.playground_2 == True:
        call epilogue from _call_epilogue
    else:
        call begining from _call_begining

label begining:

    $ persistent.lang = False

    scene bg room

    "Сегодня утро, ничего необычного вроде, пойду проверю, как семья."

    scene bg kitchen with wiperight_scene

    play music kambo_mood loop 

    c "Привет, семья."

    show m1 at l with dissolve

    m "Привет, доброго утра."
    
    show mo1 at r with dissolve

    mo "Доброго утра сынок." 

    show f1 at center with dissolve

    f "Дарова, малой."

    c "Как вы?"

    f "Да пойдет, вот только какое-то чувство..."

    c "???"

    f "Да не знаю, странное просто."

    c "Ладно, надеюсь, всё в порядке."

    scene black with fade 

    pause 3

    menu:
        "Пойти поесть.":
            jump breakfast
        "Дальше спать.":
            $ asleep = True
            scene black with fade 
            "Я пошел спать."
            pause 4
            "Ладно, пойду проверю, как там Маша."
            scene bg kitchen with fade
            show m1 at center with dissolve
            jump after

label breakfast:

    scene bg kitchen with fade

    c "Эй, Маш, есть что на завтрак?"

    show m1 at center with dissolve

    m "Конечно."

    m "Кашу будешь?"

    c "Да, давай."

    scene black with fade

    pause 3

    "Вкусно, Маша хорошо готовит."

    scene bg kitchen with fade 

    c "Очень вкусно было."

    show m1 at center with dissolve

    m "Спасибо."

    jump after

label after:
    
    c "Пошли погуляем?"

    m "Да давай."

    scene bg village with wiperight_scene

    pause 3

    "Мы пошли гулять. Не помню, когда мы в последний раз так делали, но ладно"

    show m1 at center with dissolve

    m "Как ты?"

    c "Да в порядке."

    m "Пошли покачаемся, все равно делать нечего."

    c "Пошли."

    scene bg katcheli with wiperight_scene

    show m1 at center with dissolve

    pause 2

    show m1:
        xalign 0.5 yalign 1.0
        linear 0.6 xalign 1.0

    show fl1 at l with dissolve

    "???" "Здрасьте"

    c "Мы тебя знаем?"

    #m "Мы тебя знаем?"

    "???" "Нет, но можем познакомиться."

    c "Странный ты чувак."

    m "Очень странный!"

    fl "Я Флинн."

    fl "А кто вы?"

    m "Маша."

    #m "Он не говорит, его зовут {player_name}"

    #fl "Понял"

    c "Камбо."

    fl "Хмм Камбо? Это разве русское имя?"

    c "Нет, мои родители дали мне то, что пришло в голову первым"

    fl "Вы серьезно живете в этой глуши?"

    m "Тот же вопрос к тебе."

    c "Да."

    fl "Я живу с папой, у него отказали лёгкие, поэтому я не смогу уехать."

    fl "Мне 19."

    c "Бля, чувак, мне жаль тебя. Хочешь прикол? Моя мать больна раком поджелудочной железы."
    
    #m "У нас тоже мать болеет...{w} Раком"

    "..."

    fl "...{w} Пиздец."

    c "Я про то же, но мы с Машей вроде живем."

    fl "А она проходит терапию?"

    m "НЕЕТ!"

    m "Она не хочет."

    c "Как бы мы ее не уговаривали."

    c "Слушай, может прогуляемся?"

    #m "Пошли прогуляемся?"

    fl "Давайте."

    scene bg village with fade

    show fl1 at l with dissolve

    show m1 at r with dissolve

    fl "Давайте так, мы подумаем как отвлечься, кем бы вы хотели быть?"

    fl "Я бы хотел стать полицейским, а точнее суд-мед экспертом. А вы?"

    m "Я бы хотела быть призидентом какой нибудь страны, я люблю когда на меня кладут всю ответственность."

    "Ну не фига себе, что Маша выдала, какой призидент?"

    c "Ты уверена?"

    jump continue1

label continue1:

    m "Ну ладно, а что насчет личного фронта?"

    fl "Ты про отношения? Не думаю, что они мне нужны, у меня всё-таки отец."

    m "Да, ты прав у тебя проблем полно."

    scene black with fade 

    pause 3

    scene bg village with fade

    stop music 

    show m1 at r with dissolve

    show fl1 at l with dissolve

    "Ух ты, уже вечер, пора расходится."
    
    c "Эй, ребят, может, пойдем?"

    "Флинн и Маша" "Пошли."

    fl "У качелей разойдемся?"

    c "Да давай."

    scene bg katcheli with wiperight_scene

    show m1 at r with dissolve

    show fl1 at l with dissolve

    "Вот мы и пришли."

    fl "Ладно ребят давайте, вы крутые."

    "Камбо и Маша" "Давай!"

    hide fl1 with dissolve

    "Фух...{w} Вот это паренек, жалко его и отца его, надеюсь, что все будет нормально."

    m "Пошли?"

    c "Да давай!"

    scene black with fade 

    "Мы пришли домой и я лег спать."

    window hide

    pause 3

    jump day2


label day2:

    window show 

    "Сегодня воскресенье. Завтра в школу. Кстати, а где учится Флинн? Надо его спросить потом."

    "Пойду проверю их."

    scene bg kitchen with wiperight_scene

    show f1 at center with dissolve 

    f "Привет сынок, уже проснулся?"

    c "Привет пап, а где Маша?"

    f "Она ушла гулять."

    "С кем? С Флинном?"

    c "Пап, а с кем она ушла? Он не был в белой рубашке, с русыми волосами и карими глазами?"

    f "Да, вроде он, а что, что-то случилось?"

    c "Да нет, странно, что они меня не подождали просто."

    f "Ничего сынок, думаю не просто так."

    "О чем он?"

    c "О чем ты пап?"

    f "Ну Маша уже не маленькая."

    c "Батя ей всего 15! Плюсом мы с {i}ним{/i} день знакомы!"

    f "Да я шучу, я бы освежевал его."

    "Ага-ага."

    c "А где мама?"

    f "М-мама в больнице..."

    "ЧТО БЛЯТЬ?"

    c "Стой, как это?"

    f "У нее случился приступ. Ее увезли."

    "СУКА!"

    c "Как. Мама."

    f "Она в порядке. Просто приступ, надейся на лучшее."
    
    c "Ладно, прости я пойду к ним."

label gotoem:

    scene bg village with fade

    "Вон они!"

    scene bg village at run 

    c "Стойте!{nw}"

    pause 2.3

    scene bg katcheli with fade

    show m1 at l with dissolve

    show fl1 at r with dissolve

    c "Вот вы где."

    c "Почему ушли без меня?"

    m "На самом деле мы не уходили."

    m "Я будила тебя 4 раза, а ты спал."

    fl "У нас есть темка для тебя."

    c "Темка?"

    fl "Будем помогать людям с хозяйством и нам будут платить."

    c "Ну и как мы кого-то найдем?"

    fl "Вот за этим мы тебя и искали."

    m "Мы сами пока не знаем."

    fl "Может порасспрашиваем на окраинах, там 100%% кто-то будет."

    m "Хороший план!"

    "Настолько надёжный, аж у меня волосы от ветра улетели."

    #"{color=#00FF33}Вы, трое иногда такие затупки, но сейчас не об них, мой друг.{/color}"

    c "Ладно, пошлите тогда."

    fl "Также у меня есть сюрприз."

    "Маша и Камбо" "???"

    fl "Увидите."

    "Ладно."

    #"{color=#00FF33}Впервые я говорю с {i}[system_name]{/i}, здравствуй мой друг.{/color}"

    #"{color=#00FF33}Наверное ты удивишься но, лучше закрой игру, ибо тут такие события, что я сам бы испугался.{/color}"

    #"{color=#00FF33}{i}[system_name]{/i} ты выбрал?{/color}"

    #if os_name == "Windows":
    #   "А еще поменяй ос а то буквально подписка с мусором а не ос у тебя."
    #elif os_name == "Linux":
    #   "Now we're talkin' about! напише мне на каком дистро в тг - @daoedyo"

    #menu:
    #    "Выйти":
    #        $ renpy.quit()
    #        $ persistent.playground_2
    #    "{color=#8a0303}Остаться{/color}":

    jump yntraadlbrn
    
label yntraadlbrn:

    scene black with fade

    "Мы так и никого не нашли."

    "О чём я и говорил."

    scene bg okraine with fade 

    show m1 at r with dissolve

    show fl1 at l with dissolve

    c "Ну и что дальше Флинн?"

    fl "На сегодня все, но завтра мы продолжим. О, и, кстати, мой сюрприз."

    c "Нифига."

    fl "Я создам группу, напишу. Завтра свидимся. Давайте"

    c "Давай!"

    m "Давай."

    scene black with fade 

    pause 5

    scene bg village with fade

    m "Как думаешь, когда напишет?"

    c "Да сам хз. Может, хоть щас"

    play sound phone

    window hide

    $ quick_menu = False

    $ _game_menu_screen = None     

    $ nvl_mode = "phone"

    fl_nvl "Всем привет!"

    c_nvl "Легок на помине!"

    m_nvl "Привет!"

    fl_nvl "Вы учитесь?"

    c_nvl "Да."

    fl_nvl "Завтра после школы еще поищем!"

    c_nvl "А зачем мы вообще работаем?"

    fl_nvl "На лечение родителей, ты забыл?"

    c_nvl "Да, нет."

    fl_nvl "Вот и молчи!"

    m_nvl "Харе ребят."

    c_nvl "Ладно, давай."

    fl_nvl "Давайте."

    $ nvl_mode = "classic"

    nvl clear

    $ quick_menu = True

    $ _game_menu_screen = "save"

    show m1 at center with dissolve

    c "Маш, пошли домой, мы и так много сегодня сделали." 

    m "Да, пошли я уже спать хочу.{i}*зевок*{/i} Пошли!"

    scene black with wiperight_scene

    #"Я тебя предупреждал [system_name]."

    jump day_3

label day_3:

    play sound alarm

    "Сегодня в школу."

    "Еще эта работа, странная затея вообще сама по себе."

    "Ну ничего вот заработаем, я вылечу мать."

    "Ну, я надеюсь."

    scene bg room with fade

    "Вот это помойка! Надо бы тут потом убраться."

    "Ладно, что-то я задумался, пора в школу!"

    scene bg village with wiperight_scene

    play music deepcare loop

    "???" "СТОЙ!!!"

    "Хм, даже не знаю. Кто это может быть?"

    m "Камбо, это я Маша!"

    "Не удивительно."

    show m1 at center with dissolve

    c "Ты взяла меня, сдаюсь."

    m "Заткнись!"

    m "Сегодня опять поиск работы!"

    c "Ты досих пор веришь ему? хах, ты тупее, чем я думал о тебе всю твою жизнь."

    m "Опять?"

    c "Ладно, прости."

    $ nvl_mode = "phone"

    nvl clear

    $ quick_menu = False 

    $ _game_menu_screen = None
    
    play sound phone

    pause 3

    fl_nvl "Эй, вы живы?"

    c_nvl "Нет."

    m_nvl "ДА!!!"

    c_nvl "Ладно-ладно."

    fl_nvl "Отлично!"

    fl_nvl "Значит определились, сегодня после школы."

    c_nvl "Кстати, у меня не было времени спросить, но..."

    c_nvl "Флинн, где ты учишься?"

    fl_nvl "Я? Нигде, ты забыл? Мне 18."

    c_nvl "Ну может быть колледж или типа того."

    fl_nvl "Нет, даже не хочу."

    c_nvl "А почему ты не в армии?"

    fl_nvl "У меня отсрочка, я за отцом ухаживаю."

    c_nvl "Точно!"

    m_nvl "Хм, везет вам, я бы тоже хотела пойти в армию."

    c_nvl "Не то чтобы мы этого хотели..."

    fl_nvl "Пускай рубят мне конечности! Ни ногой в армию!"

    c_nvl "+ в чат!"

    m_nvl "Ну вы и странные, вам бы лишь дома на диване лежать!"

    fl_nvl "Ладно, мы сдаемся!"

    scene black with fade 

    $ nvl_mode = "classic"

    nvl clear

    $ quick_menu = True

    $ _game_menu_screen = "save"

    pause 3

    "Пока мы чатились, мы уже подошли к школе."

    scene bg school with fade

    "Странно, здесь никого нет."

    show m1 at center with dissolve

    m "Так тихо."

    m "Так странно."

    c "Не думаешь идти вперед?"

    m "Д-да, прости."

    scene black with fade

    pause 3

    "Как всегда, обычный день. скоро звонок."

    pause 3

    play sound bell

    pause 3

    scene bg classroom with fade

    pause 3 
    
    "Все начинали уходить."

    "Все ушли, остались в классе только я, Маша."

    "Ну что же, пойдем проверим, как там Флинн."

    show m1 at center with dissolve

    c "Ну что, веселишься?"

    m "Да. Ведь скоро выйдет мама."

    c "Я надеюсь."

    play sound phone

    $ nvl_mode = "phone"

    nvl clear

    $ quick_menu = False

    $ _game_menu_screen = None

    fl_nvl "Эй, ребят, нашел добычу - какой-то старец"

    fl_nvl "Живет в богатеньком доме, весь такой добренький. Возможно он наша цель."

    c_nvl "О замечательно"

    m_nvl "Прекрасно!"

    fl_nvl "Щас кину адрес. Приходите."

    $ nvl_mode = "classic"

    nvl clear

    $ quick_menu = True

    $ _game_menu_screen = "save"

    c "Пошли туда прямо сейчас!"

    scene bg fhouse with wiperight_scene

    "Оно?"

    show m1 at center with dissolve

    m "Думаю тут."

    show m1:
        xalign 0.5 yalign 1.0
        linear 0.6 xalign 1.3

    show fl1 at l with dissolve

    fl "Вот и вы!"

    fl "Пошлите!"

    play sound housebell

    pause 3

    o "Иду!"

    show o1 at center with dissolve

    c "Эм...{w} Здраствуйте."

    o "Приветствую. Как вас зовут?"

    c "Камбо."

    m "Маша."

    fl "Флинн."

    c "А как зовут вас?"

    o "О-о-о... Неважно, как меня зовут. Пройдемте."

    scene bg fhouse1 with wiperight_scene

    o "Тут, амбар джентльмены. Не могли бы вы, принести 3 бидона в тот подвал?"

    c "Да, конечно."
    
    scene bg fambar with wiperight_scene

    c "Вон бидоны."

    scene black with fade

    pause 3

    scene bg fbasement with fade

    play sound door_closed

    c "Эй!!!"

    show fl1 at center with dissolve

    play music miracle_of_crowbar loop 

    fl "Че?"

    c "Чувак, она заперта."

    fl "Пизда."

    c "Полная."

    c "Вы меня слышите? Откройте!"

    fl "Мы уже мертвы."

    c "Чувак, на что ты нас подписал?"

    fl "Я не знал!"

    c "Ну будем сидеть, ждать счастливого момента."

    scene black with fade

    pause 10

    #"{color=#00FF33}Зря [system_name], теперь наблюдай.{/color}"

    scene bg fbasement with fade

    show fl1 at center with dissolve

    c "Чувак! Тут монтировка."

    fl "Ооо, давай, ломай эту дверь."

    scene black with fade

    play sound crashing_door

    scene fhouse with fade

    c "Где Маша?"

    c "Она внутри амбара, погнали посмотрим!"

    scene black with fade
    
    pause 3

    scene bg fambar with fade

    show m3:
        xalign 0.9 yalign 3.0

    show fl1 at l with dissolve

    c "Маша."

    m "О-он."

    fl "Успокойся, что он сделал?"

    m "Он он он."

    m "Он изнасиловал меня."

    c "Тихо сестренка, успокойся."

    c "Мне нужно отойти, ты должна быть сильной, понимаешь?"

    m "..."

    scene bg fambar with dissolve

    show fl1 at center with dissolve

    c "Ох, я освежую этого выродка и пожарю его на костре, и съем каждую крупинку его подкожного жира."

    c "Этот ублюдок пожалеет, что не убил нас, Флинн ты со мной?"

    fl "Я с тобой, не важно куда."

    #fl "Камбо стой!"

    scene bg fhouse1 with fade

    show o1 at center with dissolve

    show fl1 at l with dissolve

    o "Ну привет, как вам?"

    c "Ты кусок дерьма! Какого хера ты творишь?"

    o "Да потому что человечество сгнило!"

    o "Это они заставили меня это делать!"

    o "Мы с сыном всегда были против насилия!"

    c "Это сука не отговорка, давай я блять твоего сына выебу, а потом убью его?"

    o "Ты че сука блять! Он не смоет позор, а твоя сестра - позорный кусок дерьма, которая через пару лет сама бы стала давалкой!"

    c "Ты мразь, нихуя не разбираешься в женской психологии, я не удивлен, что у тебя жены нет!"

    o "Да ты сука не понимаешь блять! Семья это главное!"

    c "Ты прав сука! Эй, пора с этим кончать."

    show black with fade 

    o "Ай блять...!"

    play sound smash

    o "Сукааа!"

    play sound smash

    c "Ты мразь, я убью тебя!"

    play sound fall

    scene txs ground at slow_shaking

    $ renpy.music.set_volume(0.2, delay=1.5, channel='music')

    play sech shock loop

    show o1:
        align (0.5, 0.0)
        zoom 1.5
        slow_shaking_for_sprites
        

    o "{cps=100} Я тебя блять, аааа...{nw}{/cps}"

    c "На сука!"


    play sound smash

    hide o1

    show o2:
        align (0.5, 0.0)
        zoom 1.5
        slow_shaking_for_sprites

    extend " Н-на мразь!"

    play sound smash

    hide o2

    show o3:
        align (0.5, 0.0)
        zoom 1.5
        slow_shaking_for_sprites

    extend " Я тебя ненавижу!!!"

    play sound smashing

    scene bg fhouse1

    show fl1 at center with dissolve

    pause 3

    stop music fadeout 1.0

    stop sech

    c "СУКА."

    c "Мы должны уходить."

    c "Маша!"

    m "Д-да."

    c "Эй Флинн, поможешь с трупом?"

    fl "Чувак, ты ебанутый."

    menu:

        "Хах, знаю.":
            scene black with fade
            jump pizdec
        "Прости...":
            scene black with fade
            jump pizdec


label pizdec:

    scene bg fhouse1 with fade

    show fl1 at center with dissolve

    "..."

    c "Нихера, смотри - сумка с деньгами. Мы можем попробовать оплатить лечение родителям."

    fl "Ооо бери."

    c "Никому не говорите!"

    fl "Чувак..."

    c "Заткнись... Тоесть прости... Я не хотел."

    fl "Ладно, не время разглагольствовать."

    c "Ты прав... Машу совсем парализовало."

    scene bg fambar with wiperight_scene

    show fl1 at r with dissolve

    show m1 at center with dissolve

    c "Маш?"

    m "П-пошли домой, пожалуйста..."

    c "Гребанный старик совсем изжил своё и ебнулся...?"

    fl "Пошли."

    scene bg kitchen with wiperight_scene

    "Папа уехал в больницу к маме."

    show m1 at center with dissolve

    "Нужно ее уложить."

    c "Маш, пошли."

    m "Д-давай..."

    scene bg masha_room with wiperight_scene

    show m1 at center with dissolve

    "Ну ладно я спать пойду."

    m "Спокойной ночи. Я люблю тебя."

    c "Я тоже..."

    scene bg room with wiperight_scene

    "Л-ладно я пойду спать."
    
    scene black with fade

label final:

    pause 3

    "Уже утро."

    "Пойду в школу."

    scene bg village with wiperight_scene

    pause 5

    "Странно, Маша уже должна была выйти."

    pause 3

    hide window

    play sound phone

    $ quick_menu = False

    $ _game_menu_screen = None

    $ nvl_mode = "phone"

    nvl clear

    fl_nvl "Эй? Камбо? Жив?"

    c_nvl "Да."

    fl_nvl "Как Маша?"

    c_nvl "Странно, она должна была пойти в школу."

    c_nvl "Но ее нет."

    fl_nvl "Может она спит?"

    c_nvl "Скорее всего. Пойду проверю ее."

    $ quick_menu = True

    $ _game_menu_screen = "save"

    $ nvl_mode = "classic"

    scene bg kitchen with wiperight_scene

    pause 2

    scene bg masha_room with wiperight_scene

    pause 3

    c "М-мааааш?..."

    c "..."

    "Она дышит?"

    c "Маш?"

    show m2:
        align(0.5, 0.5) zoom 1.0
        linear 0.1 zoom 3.0
        linear 0.1 yalign 0.0

    play sound screamer

    pause 0.3

    scene white

    scene Error1

    $ renpy.pause(0.2, hard=True)

    scene Error

    $ renpy.pause(0.5, hard=True)

    stop sound

    scene bg masha_room 

    show m2 at center

    $ renpy.pause(1.0, hard=True)

    c "Твою мать, что это? Бисопролол? Пустой блистер."

    c "Стой НЕЕЕЕЕЕТ..."

    c "Зачем? Зачем? Мы же почти победили? СУУУУУУУУУУКАААААААА ЕБАНЫЙ ДЕЕЕЕЕД."

    c "Мааааша пожалуйста. Блять надо бежать в больницу."

    c "Алло это такси? Я живу в..."

    scene black with fade

    pause 4

    scene bg taxi2 with fade

    c "Здравствуйте мне в городскую больницу."

    t "Здравствуйте. Самая близкая к нам в Орехово-Зуево."

    c "Едьте, только быстрее!"

    scene black with fade

    pause 3

    t "Мы приехали."

    c "Спасибо, вот вам."

    t "До свидания, удачи вам."

    scene bg hosp1 with fade

    scene bg hospital with wiperight_scene

    c "ПОМОГИ..."
    
    scene bg hospital at run

    scene black with fade

    pause 4

    scene bg palata with fade 

    show med1 at center with dissolve 

    "Аййй голова..."

    "Стоп, где Маша?"

    med "Привет, ты после операции, как ты?"

    c "Чего? Какая операция?"

    med "У вас нож застрял в спине. Ты чуть не умер... Радуйся."

    c "Твою мать, какой нож?"
    
    med "Я и пришел спросить. Нам пришлось делать операцию незаконно, или ты бы умер..."

    med "Как вас зовут?"

    c "Камбо."

    med "Очень странное имя."

    med "А та девушка, кхм, которая была с вами...\nЯ соболезную, она умерла от остановки сердца.\nВ крови нашли передоз сердечными лекарствами, вы что-то знаете?"

    c "М-маша..."

    med "Ее имя Маша. Соболезную, друг."

    med "Так расскажешь, что произошло?"

    c "Я проснулся, пошел в школу, хотел с ней встретиться как обычно, но она опоздала уже на час."
    
    c "Я пришел проведать ее, но она лежала в кровати, а рядом с ней был пустой блистер с бисопрололом."
   
    med "Так, хорошо, назовите свою фамилию, пожалуйста."
    
    c "Марков."
    
    med "Марков Камбо..."
    
    c "Петрович."
   
    med "Марков Камбо Петрович, хм, у вас есть паспорт?"
   
    c "Да, возьмите."
    
    pause 3
    
    med "Угу."
    
    med "А не знаете по поводу ножа?"
   
    c "Не помню особо. Помню, что упал на что-то, но не почувствовал особо и пошел.\nУ меня врожденная анальгезия."
  
    med "У вас есть родственники и родственники той девушки?"
  
    c "Да, она моя сестра, наш отец лежит с мамой в хирургии."
 
    med "ФИО девушки, матери и отца, пожалуйста."
  
    c "Маркова Мария Петровна, Марков Петр Ярославович,\nМаркова Елена Александровна."
  
    med "Хорошо, теперь выпейте это и отдыхайте."
  
    scene black with fade
  
    "Я выпил таблетки и уснул."
   
    pause 4

    scene bg palata with fade

    show f1 at center with dissolve 

    f "Сынок..."

    c "Привет."

    f "Мне сказали, ты был 20 дней в реанимации."

    c "Я не успел, проявил халатность. Прости меня, я ужасный."

    f "Это не твоя вина..."

    c "Только моя."

    f "..."

    c "Чего ты вздыхаешь?"

    f "Мама... Умерла."

    "НЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕТ! СУКА, ВСЕ ЗРЯЯЯЯЯ!!!!!!"

    f "Сынок, что случилось? Ты в порядке?"

    f "Сыыыыыын!"

    show f1 at felt_asleep zorder 100

    show bg palata at felt_asleep zorder 100

    show black 

    pause 3

    "Я устал, пожалуй, отдохну..."

    pause 5

    scene bg palata with fade

    show med1 at center with dissolve 

    med "Ну, снова здравствуй."

    c "Здравствуйте."

    med "Хочешь, порадую тебя?"

    c "Давайте..."

    med "Завтра твоя выписка."

    c "Ага..."

    med "Ну, удачной тебе жизни тогда заранее, завтра меня не будет."

    c "Спасибо, док. А как вас зовут?"

    med "Меня-то? Павел."

    c "Спасибо, Павел."

    hide med1

    show med1 at center 

    p "Да пожалуйста, ты мой номер оставь, на всякий случай."

    c "Хорошо, давайте."

    p "Вот моя визитка, позвони, если что-то случится."

    c "Ага."

    scene black with fade

    pause 3

    scene bg hosp1 with fade

    "Вот она свобода, 26 дней я там лежал..."

    "Ладно, поеду."

    show med1 at center with dissolve 

    p "Эй!"

    "Ааа?"

    p "Тебя кто-то заберет?"

    c "Нет..."

    p "Хочешь, подвезу?"

    menu:  
        "Давайте.":
            p "Поехали."
            scene black with fade
            scene bg pavel_car with fade
            "У него неплохая тачка."
            c "У вас хорошая машина."
            p "Хах, спасибо."
            pause 3
            p "Эй, я тебя понимаю, мой отец умер недавно, а мой брат не общается со мной."
            c "Ох..."
            p "Давай заключим сделку?"
            c "Какую?"
            p "Давай проводить общие консультации, ты ментально хорош, вон какой крепкий, я бы ревел. Так что это нам обоим поможет, давай?"
            c "Давайте."
            $ deal = True
            p "Вот и отлично."
            p "Ты где живешь?"
            c "В поселке..."
            scene black with fade
            pause 3
            scene bg pavel_car with fade
            p "Понял, ладно, щас доедем."
            scene black with fade
            pause 3
            scene bg pavel_car1 with fade
            p "Все, приехали."
            c "Спасибо."
            p "Удачи тебе, парень."
            c "И вам удачи."
            scene black with fade
            pause 3 
            scene bg village with fade
            "Ох, дом, милый дом."
            jump end

        "Я просто вызову такси.":
            hide p1 with dissolve
            p "Ладно."
            pause 3
            c "Здравствуйте, можно заказать такси в Орехово-Зуево, ул. Барышникова 13?"
            "Менеджер" "Да, конечно."
            c "Ага, спасибо."
            scene black with fade
            scene bg GBUZ_MO with fade
            t "Здравствуйте. О, опять вы?"
            c "Да."
            t "Ну, садись."
            scene bg taxi with fade
            t "Ну и как ты?"
            c "Вот, из больницы вышел."
            t "А что было?"
            c "Нож в спине, разрезали и доставали. А еще умерли моя сестра и мама."
            t "Ухх, соболезную. Мой друг тоже недавно умер, у него было два сына, один врач, один школьник. И старший приказал младшему сидеть с отцом и заботиться о нем, потому что у отца были проблемы с легкими. И вот отец — мой друг — умер на днях, захлебнулся кровью, пока спал."
            c "Знаете, эта история напоминает мне кое-что, хотя я не уверен."
            t "Знаешь, а ты паренек хороший, дай-ка свой номер, потом за жизнь перетрем."
            c "Х-хорошо, вот."
            scene black with fade
            scene bg taxi with fade
            t "Ага. А тебя как зовут-то?"
            c "Камбо."
            t "Камбо, хм, странное имя."
            c "А вас как?"
            t "Алексей."
            c "Хорошее имя."
            t "Взаимно."
            t "Ты если что звони, окей?"
            c "Ага."
            $ deal_2 = True
            scene black with fade
            pause 3
            scene bg taxi2 with fade
            t "Все, приехали."
            c "Спасибо."
            t "Удачи тебе, парень."
            c "И вам удачи."
            scene black with fade
            pause 3 
            scene bg village with fade
            "Ох, дом, милый дом."
            jump end