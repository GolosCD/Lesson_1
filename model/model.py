from model.get_function import *
from model.calculation_function import *
from model.update_function import *
from view.view import *




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
                upd_qty_build(build_name, build_count_int,'+')
                
                # списываем затраты на постройку с баланса игрока
                upd_gold_player(build_count_price_float,0)

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

# =======================
#      WARNINGS
# =======================
# функция выводит уведомления о разных событиях
def warning_information(res_name):
        if res_name == 'gold':
                clear_console()#очистка консоли
                
                print(f'Need more gold!')
                input('Press Enter')                
        else:
                pass

