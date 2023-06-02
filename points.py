#default start values 
value:dict = {'farm': {'count_int': 0,
                  'price_float': 1000.00,
                  'product_per_one_float': 500}, # one farm gives 500 food in year

              'market': {'count_int': 0,
                      'price_float': 2000.00,
                      'product_per_one_float': 200},# one market gives 200 golld in year
              
              'mine': {'count_int': 0,
                      'price_float': 3000.00,
                      'product_per_one_float': 1.9},
              
              'blacksmith': {'count_int': 0,
                              'price_float': 3000.00,
                              'product_per_one_float': 1.9},
              
              'castl': {'count_int': 0,
                      'price_float': 5000.00,
                      'product_per_one_float': 1.9},
              
              'user_resurce': {'food_int': 1700,
                              'villager_int': 750,
                              'gold_float': 1500.00,
                              'taxes': 0.5},
              
              'year': {'count_int': 1,
                      'calendar_year_int': 1388,
                      'harvest_ratio_float': 0.78,
                      'year_price_food_float':85.0},
              
              'price':{'food_float': 85.0}

             }
             
#main menu items             
main_menu:dict = {
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

#build menu items
build_menu:dict = {
                   1: 'Ферма',
                   2: 'Рынок',
                   3: 'Шахты',
                   4: 'Кузница',
                   5: 'Замок',
                   0: 'Назад'
                  }
                  
#this dict translate ru_name to eng_name items menu                  
operation_name:dict = { # словарь для перевода значений введных пользователем в текст
                       '1': 'farm',
                       '2': 'market',
                       '3': 'mine',
                       '4': 'blacksmith',
                       '5': 'castl',
                      }

#this main farm menu build
farm_menu:dict = {
                  1: 'Построить ферму',
                  0: 'Назад'
                 }

#this main market menu build
market_menu:dict = {
                    1: 'Построить рынок',
                    0: 'Назад'
                   }                 