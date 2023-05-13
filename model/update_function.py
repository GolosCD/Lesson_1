from model.get_function import *


# =======================
#      UPDATE FUNCTIONS 
# (функции обновления игровых данных)
# =======================

# ----------upd_gold_player--------------------------------------------
# функция обновляет кол-ва золота у игрока
# функция принимает кол-во золота и тип операции
# если type_operation=0, то qty_gold будет списано
# если type_operation=1, то qty_gold будет начислено
from model.get_function import *
def upd_gold_player(qty_gold,type_operation):
    if type_operation == 0:
        value['user_resurce']['gold_float'] =\
            get_current_qty_gold() - qty_gold
    else:
        value['user_resurce']['gold_float'] =\
            get_current_qty_gold() + qty_gold

# ----------upd_qty_build-----------------------------------------
# функция зменяет кол-ва построек выбранного типа
# в функцию передается название постройки и кол-во и знак + или -
# на которое надо увеличить текущий показатель
def upd_qty_build(build_name, qty, mark):
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