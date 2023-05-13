import json

#Загружаем файл с дефлотным значением переменных
#file_name = 'C:\\Users\\AnanevSYU\\Documents\\01. Совещания\\2023-01-18 - Learn\\04. Python\\01.Project\\dark_imperor_md\model\\default_value.json'
file_name ='dark_emperor_md/model/default_value.json'
with open(file_name, 'r') as json_file:
    default_value=json.load(json_file)

#default start value
value = default_value

# =======================
#      GET FUNCTIONS 
# (функции показа текущего состояния игровых данных)
# =======================

# ----------get_current_price_build--------------------------------------
# функция показа текущего значения кол-ва зданий выбранного типа
# в функцию передается название типа здания, чье кол-во хотим увидитить
# функция вовзращает текущее кол-во запрощенных типов зданий
def get_current_price_build(build_name):
                return value.get(build_name).get('price_float')
            
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