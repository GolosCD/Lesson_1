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