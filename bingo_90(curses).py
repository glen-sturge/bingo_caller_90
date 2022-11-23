import random
import curses


# Constants
X_START = 5
Y_START = 5

BINGO_90_LIST = [1, 2, 3, 4, 5,
                 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15,
                 16, 17, 18, 19, 20,
                 21, 22, 23, 24, 25,
                 26, 27, 28, 29, 30,
                 31, 32, 33, 34, 35,
                 36, 37, 38, 39, 40,
                 41, 42, 43, 44, 45,
                 46, 47, 48, 49, 50,
                 51, 52, 53, 54, 55,
                 56, 57, 58, 59, 60,
                 61, 62, 63, 64, 65,
                 66, 67, 68, 69, 70,
                 71, 72, 73, 74, 75,
                 76, 77, 78, 79, 80,
                 81, 82, 83, 84, 85,
                 86, 87, 88, 89, 90]


def main(stdscr):
    # Colors Constants
    # I don't quite understand why yet, but they seem to need to be here inside the function.
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    RED_AND_BLACK = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    WHITE_AND_BLACK = curses.color_pair(2)

    # Main screen, default and blank.
    stdscr.refresh()

    # Main window. Red background, bingo label.
    main_win = curses.newwin(21, 77, Y_START, X_START)
    main_win.bkgd(" ", RED_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(1, 1, "   ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(2, 1, " B ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(3, 1, "   ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(5, 1, "   ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(6, 1, " I ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(7, 1, "   ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(9, 1, "   ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(10, 1, " N ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(11, 1, "   ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(13, 1, "   ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(14, 1, " G ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(15, 1, "   ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(17, 1, "   ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(18, 1, " O ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.addstr(19, 1, "   ", WHITE_AND_BLACK | curses.A_REVERSE)
    main_win.refresh()

    # Numbered windows for the numbers 1-90.
    num_win01 = curses.newwin(3, 2, Y_START + 1, X_START + 5)
    num_win02 = curses.newwin(3, 2, Y_START + 5, X_START + 5)
    num_win03 = curses.newwin(3, 2, Y_START + 9, X_START + 5)
    num_win04 = curses.newwin(3, 2, Y_START + 13, X_START + 5)
    num_win05 = curses.newwin(3, 2, Y_START + 17, X_START + 5)
    num_win06 = curses.newwin(3, 2, Y_START + 1, X_START + 8)
    num_win07 = curses.newwin(3, 2, Y_START + 5, X_START + 8)
    num_win08 = curses.newwin(3, 2, Y_START + 9, X_START + 8)
    num_win09 = curses.newwin(3, 2, Y_START + 13, X_START + 8)
    num_win10 = curses.newwin(3, 2, Y_START + 17, X_START + 8)
    num_win11 = curses.newwin(3, 2, Y_START + 1, X_START + 11)
    num_win12 = curses.newwin(3, 2, Y_START + 5, X_START + 11)
    num_win13 = curses.newwin(3, 2, Y_START + 9, X_START + 11)
    num_win14 = curses.newwin(3, 2, Y_START + 13, X_START + 11)
    num_win15 = curses.newwin(3, 2, Y_START + 17, X_START + 11)
    num_win16 = curses.newwin(3, 2, Y_START + 1, X_START + 14)
    num_win17 = curses.newwin(3, 2, Y_START + 5, X_START + 14)
    num_win18 = curses.newwin(3, 2, Y_START + 9, X_START + 14)
    num_win19 = curses.newwin(3, 2, Y_START + 13, X_START + 14)
    num_win20 = curses.newwin(3, 2, Y_START + 17, X_START + 14)
    num_win21 = curses.newwin(3, 2, Y_START + 1, X_START + 17)
    num_win22 = curses.newwin(3, 2, Y_START + 5, X_START + 17)
    num_win23 = curses.newwin(3, 2, Y_START + 9, X_START + 17)
    num_win24 = curses.newwin(3, 2, Y_START + 13, X_START + 17)
    num_win25 = curses.newwin(3, 2, Y_START + 17, X_START + 17)
    num_win26 = curses.newwin(3, 2, Y_START + 1, X_START + 20)
    num_win27 = curses.newwin(3, 2, Y_START + 5, X_START + 20)
    num_win28 = curses.newwin(3, 2, Y_START + 9, X_START + 20)
    num_win29 = curses.newwin(3, 2, Y_START + 13, X_START + 20)
    num_win30 = curses.newwin(3, 2, Y_START + 17, X_START + 20)
    num_win31 = curses.newwin(3, 2, Y_START + 1, X_START + 23)
    num_win32 = curses.newwin(3, 2, Y_START + 5, X_START + 23)
    num_win33 = curses.newwin(3, 2, Y_START + 9, X_START + 23)
    num_win34 = curses.newwin(3, 2, Y_START + 13, X_START + 23)
    num_win35 = curses.newwin(3, 2, Y_START + 17, X_START + 23)
    num_win36 = curses.newwin(3, 2, Y_START + 1, X_START + 26)
    num_win37 = curses.newwin(3, 2, Y_START + 5, X_START + 26)
    num_win38 = curses.newwin(3, 2, Y_START + 9, X_START + 26)
    num_win39 = curses.newwin(3, 2, Y_START + 13, X_START + 26)
    num_win40 = curses.newwin(3, 2, Y_START + 17, X_START + 26)
    num_win41 = curses.newwin(3, 2, Y_START + 1, X_START + 29)
    num_win42 = curses.newwin(3, 2, Y_START + 5, X_START + 29)
    num_win43 = curses.newwin(3, 2, Y_START + 9, X_START + 29)
    num_win44 = curses.newwin(3, 2, Y_START + 13, X_START + 29)
    num_win45 = curses.newwin(3, 2, Y_START + 17, X_START + 29)
    num_win46 = curses.newwin(3, 2, Y_START + 1, X_START + 32)
    num_win47 = curses.newwin(3, 2, Y_START + 5, X_START + 32)
    num_win48 = curses.newwin(3, 2, Y_START + 9, X_START + 32)
    num_win49 = curses.newwin(3, 2, Y_START + 13, X_START + 32)
    num_win50 = curses.newwin(3, 2, Y_START + 17, X_START + 32)
    num_win51 = curses.newwin(3, 2, Y_START + 1, X_START + 35)
    num_win52 = curses.newwin(3, 2, Y_START + 5, X_START + 35)
    num_win53 = curses.newwin(3, 2, Y_START + 9, X_START + 35)
    num_win54 = curses.newwin(3, 2, Y_START + 13, X_START + 35)
    num_win55 = curses.newwin(3, 2, Y_START + 17, X_START + 35)
    num_win56 = curses.newwin(3, 2, Y_START + 1, X_START + 38)
    num_win57 = curses.newwin(3, 2, Y_START + 5, X_START + 38)
    num_win58 = curses.newwin(3, 2, Y_START + 9, X_START + 38)
    num_win59 = curses.newwin(3, 2, Y_START + 13, X_START + 38)
    num_win60 = curses.newwin(3, 2, Y_START + 17, X_START + 38)
    num_win61 = curses.newwin(3, 2, Y_START + 1, X_START + 41)
    num_win62 = curses.newwin(3, 2, Y_START + 5, X_START + 41)
    num_win63 = curses.newwin(3, 2, Y_START + 9, X_START + 41)
    num_win64 = curses.newwin(3, 2, Y_START + 13, X_START + 41)
    num_win65 = curses.newwin(3, 2, Y_START + 17, X_START + 41)
    num_win66 = curses.newwin(3, 2, Y_START + 1, X_START + 44)
    num_win67 = curses.newwin(3, 2, Y_START + 5, X_START + 44)
    num_win68 = curses.newwin(3, 2, Y_START + 9, X_START + 44)
    num_win69 = curses.newwin(3, 2, Y_START + 13, X_START + 44)
    num_win70 = curses.newwin(3, 2, Y_START + 17, X_START + 44)
    num_win71 = curses.newwin(3, 2, Y_START + 1, X_START + 47)
    num_win72 = curses.newwin(3, 2, Y_START + 5, X_START + 47)
    num_win73 = curses.newwin(3, 2, Y_START + 9, X_START + 47)
    num_win74 = curses.newwin(3, 2, Y_START + 13, X_START + 47)
    num_win75 = curses.newwin(3, 2, Y_START + 17, X_START + 47)
    num_win76 = curses.newwin(3, 2, Y_START + 1, X_START + 50)
    num_win77 = curses.newwin(3, 2, Y_START + 5, X_START + 50)
    num_win78 = curses.newwin(3, 2, Y_START + 9, X_START + 50)
    num_win79 = curses.newwin(3, 2, Y_START + 13, X_START + 50)
    num_win80 = curses.newwin(3, 2, Y_START + 17, X_START + 50)
    num_win81 = curses.newwin(3, 2, Y_START + 1, X_START + 53)
    num_win82 = curses.newwin(3, 2, Y_START + 5, X_START + 53)
    num_win83 = curses.newwin(3, 2, Y_START + 9, X_START + 53)
    num_win84 = curses.newwin(3, 2, Y_START + 13, X_START + 53)
    num_win85 = curses.newwin(3, 2, Y_START + 17, X_START + 53)
    num_win86 = curses.newwin(3, 2, Y_START + 1, X_START + 56)
    num_win87 = curses.newwin(3, 2, Y_START + 5, X_START + 56)
    num_win88 = curses.newwin(3, 2, Y_START + 9, X_START + 56)
    num_win89 = curses.newwin(3, 2, Y_START + 13, X_START + 56)
    num_win90 = curses.newwin(3, 2, Y_START + 17, X_START + 56)

    # Assignments of all the numbered windows.
    num_win01.addstr("\n01", WHITE_AND_BLACK)
    num_win01.refresh()
    num_win02.addstr("\n02", WHITE_AND_BLACK)
    num_win02.refresh()
    num_win03.addstr("\n03", WHITE_AND_BLACK)
    num_win03.refresh()
    num_win04.addstr("\n04", WHITE_AND_BLACK)
    num_win04.refresh()
    num_win05.addstr("\n05", WHITE_AND_BLACK)
    num_win05.refresh()
    num_win06.addstr("\n06", WHITE_AND_BLACK)
    num_win06.refresh()
    num_win07.addstr("\n07", WHITE_AND_BLACK)
    num_win07.refresh()
    num_win08.addstr("\n08", WHITE_AND_BLACK)
    num_win08.refresh()
    num_win09.addstr("\n09", WHITE_AND_BLACK)
    num_win09.refresh()
    num_win10.addstr("\n10", WHITE_AND_BLACK)
    num_win10.refresh()
    num_win11.addstr("\n11", WHITE_AND_BLACK)
    num_win11.refresh()
    num_win12.addstr("\n12", WHITE_AND_BLACK)
    num_win12.refresh()
    num_win13.addstr("\n13", WHITE_AND_BLACK)
    num_win13.refresh()
    num_win14.addstr("\n14", WHITE_AND_BLACK)
    num_win14.refresh()
    num_win15.addstr("\n15", WHITE_AND_BLACK)
    num_win15.refresh()
    num_win16.addstr("\n16", WHITE_AND_BLACK)
    num_win16.refresh()
    num_win17.addstr("\n17", WHITE_AND_BLACK)
    num_win17.refresh()
    num_win18.addstr("\n18", WHITE_AND_BLACK)
    num_win18.refresh()
    num_win19.addstr("\n19", WHITE_AND_BLACK)
    num_win19.refresh()
    num_win20.addstr("\n20", WHITE_AND_BLACK)
    num_win20.refresh()
    num_win21.addstr("\n21", WHITE_AND_BLACK)
    num_win21.refresh()
    num_win22.addstr("\n22", WHITE_AND_BLACK)
    num_win22.refresh()
    num_win23.addstr("\n23", WHITE_AND_BLACK)
    num_win23.refresh()
    num_win24.addstr("\n24", WHITE_AND_BLACK)
    num_win24.refresh()
    num_win25.addstr("\n25", WHITE_AND_BLACK)
    num_win25.refresh()
    num_win26.addstr("\n26", WHITE_AND_BLACK)
    num_win26.refresh()
    num_win27.addstr("\n27", WHITE_AND_BLACK)
    num_win27.refresh()
    num_win28.addstr("\n28", WHITE_AND_BLACK)
    num_win28.refresh()
    num_win29.addstr("\n29", WHITE_AND_BLACK)
    num_win29.refresh()
    num_win30.addstr("\n30", WHITE_AND_BLACK)
    num_win30.refresh()
    num_win31.addstr("\n31", WHITE_AND_BLACK)
    num_win31.refresh()
    num_win32.addstr("\n32", WHITE_AND_BLACK)
    num_win32.refresh()
    num_win33.addstr("\n33", WHITE_AND_BLACK)
    num_win33.refresh()
    num_win34.addstr("\n34", WHITE_AND_BLACK)
    num_win34.refresh()
    num_win35.addstr("\n35", WHITE_AND_BLACK)
    num_win35.refresh()
    num_win36.addstr("\n36", WHITE_AND_BLACK)
    num_win36.refresh()
    num_win37.addstr("\n37", WHITE_AND_BLACK)
    num_win37.refresh()
    num_win38.addstr("\n38", WHITE_AND_BLACK)
    num_win38.refresh()
    num_win39.addstr("\n39", WHITE_AND_BLACK)
    num_win39.refresh()
    num_win40.addstr("\n40", WHITE_AND_BLACK)
    num_win40.refresh()
    num_win41.addstr("\n41", WHITE_AND_BLACK)
    num_win41.refresh()
    num_win42.addstr("\n42", WHITE_AND_BLACK)
    num_win42.refresh()
    num_win43.addstr("\n43", WHITE_AND_BLACK)
    num_win43.refresh()
    num_win44.addstr("\n44", WHITE_AND_BLACK)
    num_win44.refresh()
    num_win45.addstr("\n45", WHITE_AND_BLACK)
    num_win45.refresh()
    num_win46.addstr("\n46", WHITE_AND_BLACK)
    num_win46.refresh()
    num_win47.addstr("\n47", WHITE_AND_BLACK)
    num_win47.refresh()
    num_win48.addstr("\n48", WHITE_AND_BLACK)
    num_win48.refresh()
    num_win49.addstr("\n49", WHITE_AND_BLACK)
    num_win49.refresh()
    num_win50.addstr("\n50", WHITE_AND_BLACK)
    num_win50.refresh()
    num_win51.addstr("\n51", WHITE_AND_BLACK)
    num_win51.refresh()
    num_win52.addstr("\n52", WHITE_AND_BLACK)
    num_win52.refresh()
    num_win53.addstr("\n53", WHITE_AND_BLACK)
    num_win53.refresh()
    num_win54.addstr("\n54", WHITE_AND_BLACK)
    num_win54.refresh()
    num_win55.addstr("\n55", WHITE_AND_BLACK)
    num_win55.refresh()
    num_win56.addstr("\n56", WHITE_AND_BLACK)
    num_win56.refresh()
    num_win57.addstr("\n57", WHITE_AND_BLACK)
    num_win57.refresh()
    num_win58.addstr("\n58", WHITE_AND_BLACK)
    num_win58.refresh()
    num_win59.addstr("\n59", WHITE_AND_BLACK)
    num_win59.refresh()
    num_win60.addstr("\n60", WHITE_AND_BLACK)
    num_win60.refresh()
    num_win61.addstr("\n61", WHITE_AND_BLACK)
    num_win61.refresh()
    num_win62.addstr("\n62", WHITE_AND_BLACK)
    num_win62.refresh()
    num_win63.addstr("\n63", WHITE_AND_BLACK)
    num_win63.refresh()
    num_win64.addstr("\n64", WHITE_AND_BLACK)
    num_win64.refresh()
    num_win65.addstr("\n65", WHITE_AND_BLACK)
    num_win65.refresh()
    num_win66.addstr("\n66", WHITE_AND_BLACK)
    num_win66.refresh()
    num_win67.addstr("\n67", WHITE_AND_BLACK)
    num_win67.refresh()
    num_win68.addstr("\n68", WHITE_AND_BLACK)
    num_win68.refresh()
    num_win69.addstr("\n69", WHITE_AND_BLACK)
    num_win69.refresh()
    num_win70.addstr("\n70", WHITE_AND_BLACK)
    num_win70.refresh()
    num_win71.addstr("\n71", WHITE_AND_BLACK)
    num_win71.refresh()
    num_win72.addstr("\n72", WHITE_AND_BLACK)
    num_win72.refresh()
    num_win73.addstr("\n73", WHITE_AND_BLACK)
    num_win73.refresh()
    num_win74.addstr("\n74", WHITE_AND_BLACK)
    num_win74.refresh()
    num_win75.addstr("\n75", WHITE_AND_BLACK)
    num_win75.refresh()
    num_win76.addstr("\n76", WHITE_AND_BLACK)
    num_win76.refresh()
    num_win77.addstr("\n77", WHITE_AND_BLACK)
    num_win77.refresh()
    num_win78.addstr("\n78", WHITE_AND_BLACK)
    num_win78.refresh()
    num_win79.addstr("\n79", WHITE_AND_BLACK)
    num_win79.refresh()
    num_win80.addstr("\n80", WHITE_AND_BLACK)
    num_win80.refresh()
    num_win81.addstr("\n81", WHITE_AND_BLACK)
    num_win81.refresh()
    num_win82.addstr("\n82", WHITE_AND_BLACK)
    num_win82.refresh()
    num_win83.addstr("\n83", WHITE_AND_BLACK)
    num_win83.refresh()
    num_win84.addstr("\n84", WHITE_AND_BLACK)
    num_win84.refresh()
    num_win85.addstr("\n85", WHITE_AND_BLACK)
    num_win85.refresh()
    num_win86.addstr("\n86", WHITE_AND_BLACK)
    num_win86.refresh()
    num_win87.addstr("\n87", WHITE_AND_BLACK)
    num_win87.refresh()
    num_win88.addstr("\n88", WHITE_AND_BLACK)
    num_win88.refresh()
    num_win89.addstr("\n89", WHITE_AND_BLACK)
    num_win89.refresh()
    num_win90.addstr("\n90", WHITE_AND_BLACK)
    num_win90.refresh()

    # Loop, Each time hit Enter a new number 'lights up' until they are all lit.
    count = 0
    while True:
        count += 1
        # Onscreen instructions window.
        instruct_win = curses.newwin(1, 35, Y_START - 1, X_START + 20)
        instruct_win.addstr("Press Enter For A New Ball Number!", curses.A_REVERSE)
        instruct_win.refresh()

        if 26 <= count < 36:
            main_win.addstr(19, 62, "Anyone Close?",  WHITE_AND_BLACK | curses.A_REVERSE)
            main_win.refresh()
        elif 36 <= count < 51:
            main_win.addstr(19, 62, "Still No one?",  WHITE_AND_BLACK | curses.A_REVERSE)
            main_win.refresh()
        elif 51 <= count < 76:
            main_win.addstr(19, 62, "    Anyone?  ",  WHITE_AND_BLACK | curses.A_REVERSE)
            main_win.refresh()
        elif 76 <= count < 91:
            main_win.addstr(19, 62, "Are We Awake?", WHITE_AND_BLACK | curses.A_REVERSE)
            main_win.refresh()
        elif count == 91:
            main_win.addstr(19, 62, "  GAME OVER  ",  WHITE_AND_BLACK | curses.A_REVERSE)
            main_win.refresh()

        # Hold, wait for Enter.
        main_win.getch()

        # Choose a number at random.
        if BINGO_90_LIST:
            select = random.randint(0, (len(BINGO_90_LIST) - 1))
            called_number = BINGO_90_LIST.pop(select)

        else:
            break

        # Display the last called number.
        # called_win = curses.newwin(1, 20, 4, 23)
        main_win.addstr(1, 59, f" #'s Called : {count:>2d} ", WHITE_AND_BLACK | curses.A_REVERSE)
        main_win.addstr(3, 59, f" This #     : {called_number:>2} ", WHITE_AND_BLACK | curses.A_REVERSE)
        if count > 1:
            main_win.addstr(5, 59, f" Last #     : {last:>2} ", WHITE_AND_BLACK | curses.A_REVERSE)
        last = called_number
        main_win.refresh()



        # Modify the called number window to be 'lit up'.
        if called_number == 1:
            num_win01.clear()
            num_win01.addstr("\n01", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win01.refresh()
        elif called_number == 2:
            num_win02.clear()
            num_win02.addstr("\n02", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win02.refresh()
        elif called_number == 3:
            num_win03.clear()
            num_win03.addstr("\n03", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win03.refresh()
        elif called_number == 4:
            num_win04.clear()
            num_win04.addstr("\n04", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win04.refresh()
        elif called_number == 5:
            num_win05.clear()
            num_win05.addstr("\n05", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win05.refresh()
        elif called_number == 6:
            num_win06.clear()
            num_win06.addstr("\n06", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win06.refresh()
        elif called_number == 7:
            num_win07.clear()
            num_win07.addstr("\n07", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win07.refresh()
        elif called_number == 8:
            num_win08.clear()
            num_win08.addstr("\n08", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win08.refresh()
        elif called_number == 9:
            num_win09.clear()
            num_win09.addstr("\n09", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win09.refresh()
        elif called_number == 10:
            num_win10.clear()
            num_win10.addstr("\n10", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win10.refresh()
        elif called_number == 11:
            num_win11.clear()
            num_win11.addstr("\n11", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win11.refresh()
        elif called_number == 12:
            num_win12.clear()
            num_win12.addstr("\n12", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win12.refresh()
        elif called_number == 13:
            num_win13.clear()
            num_win13.addstr("\n13", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win13.refresh()
        elif called_number == 14:
            num_win14.clear()
            num_win14.addstr("\n14", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win14.refresh()
        elif called_number == 15:
            num_win15.clear()
            num_win15.addstr("\n15", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win15.refresh()
        elif called_number == 16:
            num_win16.clear()
            num_win16.addstr("\n16", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win16.refresh()
        elif called_number == 17:
            num_win17.clear()
            num_win17.addstr("\n17", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win17.refresh()
        elif called_number == 18:
            num_win18.clear()
            num_win18.addstr("\n18", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win18.refresh()
        elif called_number == 19:
            num_win19.clear()
            num_win19.addstr("\n19", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win19.refresh()
        elif called_number == 20:
            num_win20.clear()
            num_win20.addstr("\n20", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win20.refresh()
        elif called_number == 21:
            num_win21.clear()
            num_win21.addstr("\n21", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win21.refresh()
        elif called_number == 22:
            num_win22.clear()
            num_win22.addstr("\n22", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win22.refresh()
        elif called_number == 23:
            num_win23.clear()
            num_win23.addstr("\n23", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win23.refresh()
        elif called_number == 24:
            num_win24.clear()
            num_win24.addstr("\n24", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win24.refresh()
        elif called_number == 25:
            num_win25.clear()
            num_win25.addstr("\n25", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win25.refresh()
        elif called_number == 26:
            num_win26.clear()
            num_win26.addstr("\n26", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win26.refresh()
        elif called_number == 27:
            num_win27.clear()
            num_win27.addstr("\n27", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win27.refresh()
        elif called_number == 28:
            num_win28.clear()
            num_win28.addstr("\n28", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win28.refresh()
        elif called_number == 29:
            num_win29.clear()
            num_win29.addstr("\n29", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win29.refresh()
        elif called_number == 30:
            num_win30.clear()
            num_win30.addstr("\n30", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win30.refresh()
        elif called_number == 31:
            num_win31.clear()
            num_win31.addstr("\n31", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win31.refresh()
        elif called_number == 32:
            num_win32.clear()
            num_win32.addstr("\n32", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win32.refresh()
        elif called_number == 33:
            num_win33.clear()
            num_win33.addstr("\n33", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win33.refresh()
        elif called_number == 34:
            num_win34.clear()
            num_win34.addstr("\n34", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win34.refresh()
        elif called_number == 35:
            num_win35.clear()
            num_win35.addstr("\n35", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win35.refresh()
        elif called_number == 36:
            num_win36.clear()
            num_win36.addstr("\n36", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win36.refresh()
        elif called_number == 37:
            num_win37.clear()
            num_win37.addstr("\n37", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win37.refresh()
        elif called_number == 38:
            num_win38.clear()
            num_win38.addstr("\n38", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win38.refresh()
        elif called_number == 39:
            num_win39.clear()
            num_win39.addstr("\n39", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win39.refresh()
        elif called_number == 40:
            num_win40.clear()
            num_win40.addstr("\n40", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win40.refresh()
        elif called_number == 41:
            num_win41.clear()
            num_win41.addstr("\n41", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win41.refresh()
        elif called_number == 42:
            num_win42.clear()
            num_win42.addstr("\n42", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win42.refresh()
        elif called_number == 43:
            num_win43.clear()
            num_win43.addstr("\n43", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win43.refresh()
        elif called_number == 44:
            num_win44.clear()
            num_win44.addstr("\n44", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win44.refresh()
        elif called_number == 45:
            num_win45.clear()
            num_win45.addstr("\n45", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win45.refresh()
        elif called_number == 46:
            num_win46.clear()
            num_win46.addstr("\n46", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win46.refresh()
        elif called_number == 47:
            num_win47.clear()
            num_win47.addstr("\n47", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win47.refresh()
        elif called_number == 48:
            num_win48.clear()
            num_win48.addstr("\n48", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win48.refresh()
        elif called_number == 49:
            num_win49.clear()
            num_win49.addstr("\n49", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win49.refresh()
        elif called_number == 50:
            num_win50.clear()
            num_win50.addstr("\n50", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win50.refresh()
        elif called_number == 51:
            num_win51.clear()
            num_win51.addstr("\n51", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win51.refresh()
        elif called_number == 52:
            num_win52.clear()
            num_win52.addstr("\n52", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win52.refresh()
        elif called_number == 53:
            num_win53.clear()
            num_win53.addstr("\n53", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win53.refresh()
        elif called_number == 54:
            num_win54.clear()
            num_win54.addstr("\n54", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win54.refresh()
        elif called_number == 55:
            num_win55.clear()
            num_win55.addstr("\n55", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win55.refresh()
        elif called_number == 56:
            num_win56.clear()
            num_win56.addstr("\n56", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win56.refresh()
        elif called_number == 57:
            num_win57.clear()
            num_win57.addstr("\n57", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win57.refresh()
        elif called_number == 58:
            num_win58.clear()
            num_win58.addstr("\n58", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win58.refresh()
        elif called_number == 59:
            num_win59.clear()
            num_win59.addstr("\n59", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win59.refresh()
        elif called_number == 60:
            num_win60.clear()
            num_win60.addstr("\n60", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win60.refresh()
        elif called_number == 61:
            num_win61.clear()
            num_win61.addstr("\n61", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win61.refresh()
        elif called_number == 62:
            num_win62.clear()
            num_win62.addstr("\n62", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win62.refresh()
        elif called_number == 63:
            num_win63.clear()
            num_win63.addstr("\n63", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win63.refresh()
        elif called_number == 64:
            num_win64.clear()
            num_win64.addstr("\n64", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win64.refresh()
        elif called_number == 65:
            num_win65.clear()
            num_win65.addstr("\n65", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win65.refresh()
        elif called_number == 66:
            num_win66.clear()
            num_win66.addstr("\n66", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win66.refresh()
        elif called_number == 67:
            num_win67.clear()
            num_win67.addstr("\n67", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win67.refresh()
        elif called_number == 68:
            num_win68.clear()
            num_win68.addstr("\n68", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win68.refresh()
        elif called_number == 69:
            num_win69.clear()
            num_win69.addstr("\n69", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win69.refresh()
        elif called_number == 70:
            num_win70.clear()
            num_win70.addstr("\n70", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win70.refresh()
        elif called_number == 71:
            num_win71.clear()
            num_win71.addstr("\n71", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win71.refresh()
        elif called_number == 72:
            num_win72.clear()
            num_win72.addstr("\n72", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win72.refresh()
        elif called_number == 73:
            num_win73.clear()
            num_win73.addstr("\n73", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win73.refresh()
        elif called_number == 74:
            num_win74.clear()
            num_win74.addstr("\n74", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win74.refresh()
        elif called_number == 75:
            num_win75.clear()
            num_win75.addstr("\n75", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win75.refresh()
        elif called_number == 76:
            num_win76.clear()
            num_win76.addstr("\n76", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win76.refresh()
        elif called_number == 77:
            num_win77.clear()
            num_win77.addstr("\n77", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win77.refresh()
        elif called_number == 78:
            num_win78.clear()
            num_win78.addstr("\n78", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win78.refresh()
        elif called_number == 79:
            num_win79.clear()
            num_win79.addstr("\n79", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win79.refresh()
        elif called_number == 80:
            num_win80.clear()
            num_win80.addstr("\n80", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win80.refresh()
        elif called_number == 81:
            num_win81.clear()
            num_win81.addstr("\n81", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win81.refresh()
        elif called_number == 82:
            num_win82.clear()
            num_win82.addstr("\n82", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win82.refresh()
        elif called_number == 83:
            num_win83.clear()
            num_win83.addstr("\n83", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win83.refresh()
        elif called_number == 84:
            num_win84.clear()
            num_win84.addstr("\n84", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win84.refresh()
        elif called_number == 85:
            num_win85.clear()
            num_win85.addstr("\n85", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win85.refresh()
        elif called_number == 86:
            num_win86.clear()
            num_win86.addstr("\n86", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win86.refresh()
        elif called_number == 87:
            num_win87.clear()
            num_win87.addstr("\n87", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win87.refresh()
        elif called_number == 88:
            num_win88.clear()
            num_win88.addstr("\n88", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win88.refresh()
        elif called_number == 89:
            num_win89.clear()
            num_win89.addstr("\n89", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win89.refresh()
        elif called_number == 90:
            num_win90.clear()
            num_win90.addstr("\n90", WHITE_AND_BLACK | curses.A_REVERSE)
            num_win90.refresh()

    # Hold screen one more time before exit.
    stdscr.getch()


if __name__ == '__main__':
    curses.wrapper(main)
