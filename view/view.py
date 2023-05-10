from controller.controller import *
from model.model import *
import sys
import os


# функция печати пунктов основного меню
def print_main_menu():
        clear_console() # очистка консоли
        for key in main_menu.keys():
                print(key, '-', main_menu[key])
        choice = input_validate('num')
        exec_menu(choice)
        return


# функция печати отчета за прошлый год

# функция печати пунктов меню постройки
def print_exeuct_build_menu(build_name):
        clear_console() # очистка консоли
        print(f'1 - Построить {build_name}.')
        print(f'0 - Назад')
        choice = input_validate('num')
        building_menu_actions[choice](build_name)
        return



# функция печати пунктов строительного меню
def print_build_menu():
        clear_console() # очистка консоли

        for key in build_menu.keys():
                print(key, '-', build_menu[key])
                
        choice = input_validate('num')
        
        if choice in operation_name.keys():
                build_name = operation_name[choice]
                
                build_menu_actions.get(choice)(build_name)
        else:
                print_main_menu()
        return


def main_menu_next_year():
        print('Функция окончания года еще не реализована')
        choice = input_validate('num')
        exec_menu(choice)
        return

def main_menu_trade_menu():
        choice = input_validate('num')
        print('Функция торговли еще не реализована')
        exec_menu(choice)
        return

def main_menu_army_menu():
        print('Функция армии еще не реализована')
        choice = input_validate('num')
        exec_menu(choice)
        return

def main_menu_food_menu():
        print('Функция пищи еще не реализована')
        choice = input_validate('num')
        exec_menu(choice)
        return

def main_menu_taxes_menu():
        print('Функция налогов еще не реализована')
        choice = input_validate('num')
        exec_menu(choice)
        return

def main_menu_assistent_menu():
        print('Функция консультанта еще не реализована')
        choice = input_validate('num')
        exec_menu(choice)
        return

def main_menu_report_menu():
        print('Функция отчета еще не реализована')
        choice = input_validate('num')
        exec_menu(choice)
        return

def main_menu_game_menu():
        print('Функция игра еще не реализована')
        choice = input_validate('num')
        exec_menu(choice)
        return


# Execute menu
def exec_menu(choice):
        clear_console() # очистка консоли
        ch = choice.lower()
        if ch == '':
                menu_actions['print_main_menu']()
        else:
                try:
                        menu_actions[ch]()
                except KeyError:
                        print("Invalid selection, please try again.\n")
                        menu_actions['print_main_menu']()
        return

# Back to main menu
def back():
        menu_actions['print_main_menu']()

# Exit program
def exit():
        sys.exit()
        
def clear_console():
        print("\n" * 3)

main_menu = {
            1: 'Следующий год',
            2: 'Строить',
            3: 'Торговля',
            4: 'Армия',
            5: 'Пища',
            6: 'Налоги',
            7: 'Консультант',
            8: 'Отчет',
            9: 'Игра'
        }        
menu_actions = {}
build_menu = {
    1: 'Ферма',
    2: 'Рынок',
    3: 'Шахты',
    4: 'Кузница',
    5: 'Замок',
    0: 'Назад'
}
menu_actions = {
    'print_main_menu': print_main_menu,
    '1': main_menu_next_year,
    '2': print_build_menu,
    '3': main_menu_trade_menu,
    '4': main_menu_army_menu,
    '5': main_menu_food_menu,
    '6': main_menu_taxes_menu,
    '7': main_menu_assistent_menu,
    '8': main_menu_report_menu,
    '9': main_menu_game_menu,
    '0': back,
    '11': exit,
}
build_menu_actions = {            # Строительство пукты меню:
    '1': print_exeuct_build_menu, # фермы
    '2': print_exeuct_build_menu, # рыноки
    '3': print_exeuct_build_menu, # шахты
    '4': print_exeuct_build_menu, # кузнецы
    '5': print_exeuct_build_menu, # замок
    '0': print_main_menu,         # back
}
building_menu_actions = {
    '1': building,
    '0': print_build_menu,
}
main_menu = {
    1: 'Следующий год',
    2: 'Строить',
    3: 'Торговля',
    4: 'Армия',
    5: 'Пища',
    6: 'Налоги',
    7: 'Консультант',
    8: 'Отчет',
    9: 'Игра'
}

build_menu = {
    1: 'Ферма',
    2: 'Рынок',
    3: 'Шахты',
    4: 'Кузница',
    5: 'Замок',
    0: 'Назад'
}

operation_name = { # словарь для перевода значений введных пользователем в текст
    '1': 'farm',
    '2': 'market',
    '3': 'mine',
    '4': 'blacksmith',
    '5': 'castl',
}

farm_menu = {
 1: 'Построить ферму',
 0: 'Назад'
}

market_menu = {
 1: 'Построить рынок',
 0: 'Назад'
}

if __name__=='__main__':
        print_main_menu()
        print_exeuct_build_menu()
        print_build_menu()
        main_menu_next_year()
        main_menu_trade_menu()
        main_menu_army_menu()
        main_menu_food_menu()
        main_menu_taxes_menu()
        main_menu_taxes_menu()
        main_menu_assistent_menu()
        main_menu_report_menu()
        main_menu_game_menu()
        exec_menu()
        back()
        exit()
        clear_console()

