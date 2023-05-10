from model import model as m

# import model.model as m 
import json

print(json.dumps(m.default_value, sort_keys=True, indent=4, ))