define c = Character('Celia', show_two_window=True, color="#dfdfdf")
define t = Character('Toma', show_two_window=True, color="#dfdfdf")
define m = Character('Meadow', show_two_window=True, color="#dfdfdf")
define k = Character('Kenta', show_two_window=True, color="#dfdfdf")
define who = Character('???', show_two_window=True, color="#dfdfdf")
define n = Character('Nyu', show_two_window=True, color="#dfdfdf")
define speaker = Character('Speaker', show_two_window=True, color="#dfdfdf")
define librarian = Character('Librarian', show_two_window=True, color="#dfdfdf")
define mans_voice = Character('Man\'s Voice', show_two_window=True, color="#dfdfdf")
define other_man = Character('Other Man', show_two_window=True, color="#dfdfdf")
define elderly_a = Character('Elderly Man', show_two_window=True, color="#dfdfdf")
define elderly_b = Character('Elderly Woman', show_two_window=True, color="#dfdfdf")
define nurse = Character('Nurse', show_two_window=True, color="#dfdfdf")

label start:

    $direct_cafeteria = 0
    $white_book = 0
    $green_book = 0
    $yellow_book = 0
    $lunch_usual = 0
    $lunch_special = 0
    
    jump c01
