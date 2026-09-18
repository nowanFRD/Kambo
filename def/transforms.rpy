init 1:
    
    transform run:
        parallel:
            zoom 1.0
            align (0.5, 0.5)
            easein 2.3 zoom 1.6
        parallel:
            easein 0.2 yoffset 5
            easein 0.2 xoffset 5
            easein 0.2 yoffset -5
            easein 0.2 xoffset -5
            repeat
        
    transform l:
        anchor (0.5, 0.5)
        xalign -0.4 yalign 1.0

    transform r:
        anchor (0.5, 0.5)
        xalign 1.5 yalign 1.0

    transform slow_shaking:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.1
        block:
            ease 3.0 pos (0.507, 0.497)
            ease 3.0 pos (0.497, 0.507)
            ease 3.0 pos (0.509, 0.496)
            ease 3.0 pos (0.496, 0.509)
            repeat
        
    transform slow_shaking_for_sprites:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        block:
            ease 3.0 pos (0.507, 0.497)
            ease 3.0 pos (0.497, 0.507)
            ease 3.0 pos (0.509, 0.496)
            ease 3.0 pos (0.496, 0.509)
            repeat

    transform changed:
        matrixcolor SaturationMatrix(0.0)

    transform felt_asleep:
        linear 0.6 alpha 0.8
        pause 0.5
        linear 0.6 alpha 0.6
        pause 0.5
        linear 0.6 alpha 0

    define slow_dissolve = Dissolve(3.0)

    define wiperight_scene = MultipleTransition([False, wiperight, Solid("#000000"), Pause(1.0), Solid("#000000"), wiperight, True])