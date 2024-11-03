def en_polsar_boto_a():
    global forma
    forma += 1
    if forma == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif forma == 2:
        basic.show_icon(IconNames.SQUARE)
    elif forma == 3:
        basic.show_icon(IconNames.SCISSORS)
    else:
        forma = 0
input.on_button_pressed(Button.A, en_polsar_boto_a)

def en_moure_el_dispositiu():
    global parar
    parar = randint(1, 3)
    if parar == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif parar == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, en_moure_el_dispositiu)

def en_polsar_boto_b():
    global forma_bot
    forma_bot = randint(1, 3)
    if forma_bot == 1 and forma == 1:
        basic.show_string("EMPAT")
    elif forma_bot == 2 and forma == 2:
        basic.show_string("EMPAT")
    elif forma_bot == 3 and forma == 3:
        basic.show_string("EMPAT")
    elif forma_bot == 1 and forma == 3:
        basic.show_string("HAS PERDUT")
    elif forma_bot == 2 and forma == 1:
        basic.show_string("HAS PERDUT")
    elif forma_bot == 3 and forma == 2:
        basic.show_string("HAS PERDUT")
    else:
        basic.show_string("HAS GUANYAT")
input.on_button_pressed(Button.B, en_polsar_boto_b)

forma_bot = 0
parar = 0
forma = 0
basic.show_string("JOC")
basic.show_icon(IconNames.SMALL_SQUARE)
basic.show_icon(IconNames.SQUARE)
basic.show_icon(IconNames.SCISSORS)
