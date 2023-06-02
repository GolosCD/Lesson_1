# -*- coding: utf-8 -*-
# Import the modules needed to run the script.
import sys
import os
import random
from points import *

# Main definition - constants
menu_actions:dict = dict()

# =======================
#      WARNINGS
# =======================
# функция выводит уведомления о разных событиях
def warning_information(res_name:str):
        if res_name == 'gold':
                clear_console()#очистка консоли
                
                print(f'Need more gold!')
                input('Press Enter')                
        else:
                pass
        
# =======================
#      VALIDATE
# =======================        
        
# ----------input_validate-----------------------------------------
# функция проверки введенного значения пользователем
# функция принимает один парамет который принимает два аргумента num и txt
# аргумент num указывается там, где мы вводим числа
# аргумент txt указывается там, где мы вводим строковые данные
# после валидации введенного значения функция его возвращает обратно
def input_validate(val):
        flag = True

        if val == 'num':
                # запускаем цикл, где будет проверяться введеное занчение
                while flag:
                        input_num = input(' >> ')
                        if input_num.isdigit():
                                return input_num
                        else:
                                try:
                                        print('Invalid input, try again')
                                except:
                                        print('Invalid input, try again')

                
        elif val == 'txt':
                # запускаем цикл, где будет проверяться введеное занчение
                while flag:
                        input_txt = input(' >> ')
                        if input_txt.isalpha():
                                return input_txt
                        else:
                                print('Invalid input, try again')
        flag = False


# =======================
#      CALC PARAM
# =======================
# ----------calc_param_build--------------------------------------------
# функция расчета затрат на постройку введенных зданий
# в функцию передается название здания и кол-во
# функция возвращает сумму за запрощенные постройки
def calc_cost_build(build_name:str, qty:int):
        return float(qty) * value.get(build_name).get('price_float')

# ----------calc_cost_build--------------------------------------------
# функция списания денежных средств со счета
# в функцию передается сумма для списания
# функция отнимает сумму списания от суммы на балансе игрока
def write_off_player_gold(price:float):
        value['user_resurce']['gold_float'] =\
            get_current_qty_gold() - price
            
# ----------calc_cost_build--------------------------------------------
# функция списания денежных средств со счета
# в функцию передается сумма для списания
# функция отнимает сумму списания от суммы на балансе игрока
def add_gold(gold:float):
        value['user_resurce']['gold_float'] =\
            get_current_qty_gold() + gold            

# ----------get_current_qty_build--------------------------------------
# функция показа текущего значения кол-ва зданий выбранного типа
# в функцию передается название типа здания, чье кол-во хотим увидитить
# функция вовзращает текущее кол-во запрощенных типов зданий
def get_current_qty_build(build_name):
                return value.get(build_name).get('count_int')
        
# ----------get_current_qty_gold---------------------------------------
# функция показывает текущее значение золота на балансе игрока
# в функцию не нужно ничего передавать
# функция возвращает значение во float
def get_current_qty_gold():
        return value.get('user_resurce').get('gold_float')

# ----------calc_harvest_ratio-----------------------------------------
# функция расчитывает коэффициент урожайности для каждого года
# коэффициент расчитывается случайномы образом с помошью библиотеки random
# функция возвращает значение в переменную harvest_ratio из словаря value
# Коэффициент урожайности должен зависить от сложности уровня!!!(не реализовано)
# Пока реализация урожайности в диапазоне от 0.0 до 1.0 может это жестко?
def calc_harvest_ratio():
        #return random.uniform(0.26, 1.0)
        value['year']['harvest_ratio_float'] =\
            random.random()

# ----------calc_year_price_food_float-----------------------------------------
# функция расчитывает цену на еду в зависимости от урожайности
# чем выше урожайность, тем больше еды, тем меньше она нужна всем
# и тем ниже устанавливаются цена на нее
# коэффициент расчитывается в зависимости от harvest_ratio_float
# функция возвращает значение в переменную year_price_food_float в словаре value
def calc_year_price_food_float():
        #расчет детерминированного коээффициента влияния урожая на цену на рынке
        determin_ratio = 1 - value['year']['harvest_ratio_float']
        #скорректированая цена будет округляться, и цена не должна быть выше 85.0
        value['year']['year_price_food_float'] =\
            min(round(determin_ratio * value['price']['food_float']\
            +value['price']['food_float']*0.32,0),value['price']['food_float'])

# ----------chang_count_build-----------------------------------------
# функция зменяет кол-ва построек выбранного типа
# в функцию передается название постройки и кол-во и знак + или -
# на которое надо увеличить текущий показатель
def chang_count_build(build_name, qty, mark):
        if mark == '+': # если + то операция увеличения кол-ва зданий
                value[build_name]['count_int'] =\
                    value.get(build_name).get('count_int') + qty
        elif mark == '-': # если минус, то операция уменьшеня кол-ва зданий
                if get_current_qty_build(build_name) >= qty:
                        value[build_name]['count_int'] =\
                            value.get(build_name).get('count_int') - qty
                else: # если зданий меньше чем мы хотим уменьшить то просто 0
                        value[build_name]['count_int'] = 0
        else:
                try:
                        print('Invalid input mark')
                except KeyError:
                        print('Invalid input mark, please try again.\n')

# ----------building-------------------------------------------------
# функция постройки игровых зданий
# в функцию передается название строения которое мы хотим построить
# функция просит ввести кол-во зданий для постройки
# функция проверяет хватает ли золота на такое кол-во построек
# если золота достаточно, то функция списывает стоимсть за постройку с баланса игрока
# функция прибавляет введенное кол-во зданий к уже имеющемуся кол-ву
def building(build_name):

        # выводим сообщение о текущем кол-ве выбранных зданий
        print('Now you have', get_current_qty_build(build_name), build_name)
        print()

        # просим ввести требуемое кол-во зданий для постройки
        build_count_int = int(
            input('Enter the number of you want to build: >> '))
        print()

        # стоимость за постройку указанных зданий сохраняем в переменной
        build_count_price_float = calc_cost_build(
            build_name, build_count_int)
        
        # проверяем есть ли на балансе нужная сумма, если есть...
        if build_count_price_float <= get_current_qty_gold():
                
                # прибавляем ввденное кол-во зданий к текущему кол-ву
                chang_count_build(build_name, build_count_int,'+')
                
                # списываем затраты на постройку с баланса игрока
                write_off_player_gold(build_count_price_float)

                # выводим сообщение об успешности, обновленное кол-во выбранных зданий
                # выводим сообщение о потраченном золоте
                # и ожидаем вода Enter для возврата в меню постройки
                print('Success! Now you have ',
                      get_current_qty_build(build_name), build_name)
                print()
                print('You have spent', build_count_price_float, 'gold.')
                input('Press Enter')

                # возвращаем игрока в меню строительства
                print_build_menu()

        else:  # обработка ошибок ввода
                try:
                        warning_information('gold')
                        print_build_menu()
                except KeyError:
                        print("Invalid selection, please try again.\n")
                        print_build_menu()

# ----------calc_end_year-------------------------------------------
# функция завершения года
# в ней запускается подсчет доходов казны, урожая, приток населения
# функция выводит на печать итоги завершенного года
def calc_end_year():
        # расчет урожая
        # расчет рандомного коэффициента урожайности
        calc_harvest_ratio()
        # расчет урожаю по окончанию года
        food = int(value['farm']['count_int'] * value['farm']['product_per_one_float']\
            * value['year']['harvest_ratio_float'])
        value['user_resurce']['food_int'] +=food
            
        # расчет цены за еденицу еды
        calc_year_price_food_float()
        # начисления налогов
        #market taxes
        profit_taxes = (value['market']['product_per_one_float']*value['market']['count_int'])*value['user_resurce']['taxes']
        # прибыль с замков, 1 замок дает 500 золота в конце года
        profit_taxes += 500*value['castl']['count_int']
        # запись прибыли 
        add_gold(profit_taxes)
        
        # расчет прироста населения
        villager = int(value['user_resurce']['villager_int'] * 0.1)
        value['user_resurce']['villager_int']+=villager
        # увеличение календарного года 
        value['year']['calendar_year_int']+=1
        new_year = value['year']['calendar_year_int']
        
        # печать годовых итогов
        print('===================================')
        print(f'Начинается {new_year} год.')
        print(f'Выполучили: {profit_taxes} золота в виде налогов')
        print(f'Выполучили: {food} едениц еды')
        print(f'Выполучили: {food} едениц еды')
        print(f'Прирост населения в этом году: {villager} человек')
        print('===================================')
        

    
# =======================
#      PRINT FUNC
# =======================

#------------------------------------------------------------------
# функция проверки введенных значений
# на вход подается значение если оно удовлетворяет условиям,
# то выполнение программы продолжнается, иначе повторнный ввод


# =======================
#      BUILD MENU
# =======================

#-----------------------------------------------------------------
# функция печати отчета за прошлый год

# функция печати пунктов меню постройки
def print_exeuct_build_menu(build_name):
        clear_console() # очистка консоли
        print(f'1 - Построить {build_name}.')
        print(f'0 - Назад')
        choice = input_validate('num')
        building_menu_actions[choice](build_name)
        return

# функция печати пунктов основного меню
def print_main_menu():
        clear_console() # очистка консоли
        for key in main_menu.keys():
                print(key, '-', main_menu[key])
        choice = input_validate('num')
        exec_menu(choice)
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
        input('Для расчета прибыли за год нажмите Enter...')
        calc_end_year()
        print()
        input('Пропустить итоги и вернуться в меню Enter...')
        choice = '0'#возврат в меню
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


# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
        print_main_menu()
