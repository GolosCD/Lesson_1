# test json config
import json
'''
value = {'farm': {'count_int': 1,
                  'price_float': 1000.00,
                  'product_per_one_float': 1.3},

         'market': {'count_int': 1,
                  'price_float': 1500.00,
                  'product_per_one_float': 1.5},

         'mine': {'count_int': 1,
                  'price_float': 1900.00,
                  'product_per_one_float': 1.9},

         'blacksmith': {'count_int': 1,
                        'price_float': 1900.00,
                        'product_per_one_float': 1.9},

         'castl': {'count_int': 1,
                  'price_float': 5000.00,
                  'product_per_one_float': 1.9},

          'user_resurce': {'gold_float': 20000.00},

          'year': {'count_int': 1,
                   'calendar_year_int': 1388}

         }

a = 56

with open(f"config{a}.json", "w") as outfile:
    json.dumps(value, sort_keys=True, indent=4, outfile)
'''    

j = open('default_value.json')

data = json.load(j)

print(json.dumps(data, sort_keys=True, indent=4, ))

#print(type(data['farm']['price_float']))

'''
value = {'farm': {'count_int': 1,
                  'price_float': 1000.00,
                  'product_per_one_float': 1.3},

         'market': {'count_int': 1,
                  'price_float': 1500.00,
                  'product_per_one_float': 1.5},

         'mine': {'count_int': 1,
                  'price_float': 1900.00,
                  'product_per_one_float': 1.9},

         'blacksmith': {'count_int': 1,
                        'price_float': 1900.00,
                        'product_per_one_float': 1.9},

         'castl': {'count_int': 1,
                  'price_float': 5000.00,
                  'product_per_one_float': 1.9},

          'user_resurce': {'gold_float': 20000.00},

          'year': {'count_int': 1,
                   'calendar_year_int': 1388}

         }

print(json.dumps(value, sort_keys=True, indent=4, ))
'''