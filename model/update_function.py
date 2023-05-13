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

