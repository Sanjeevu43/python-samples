import json
from datetime import datetime, date, time

class ComplexEncoder(json.JSONEncoder):   

    def default(self, o):
        # --- Handle sets ---
        if isinstance(o, set):
            return list(o)
        # --- Handle datetime, date, and time objects ---
        # if isinstance(o, (datetime, date, time)):
        #     return o.isoformat()

        return super().default(o)

paylod_message = {
    "batch_id": 123,
    "courses": {"M","P","C"}, # A set
    "student_names": ["A","B","C"]
}

json_string = json.dumps(paylod_message, cls=ComplexEncoder, indent=4)
print(json_string)

# with open('./myjson2','w') as write_file:
#     json.dump(paylod_message,write_file,cls=custom_obj,indent=2)

# with open('./myjson2','r') as read_file:
#     loaded_data = json.load(read_file)


#=============================================================================================
class CustomSetDecoder(json.JSONDecoder):
    def __init__(self):       
        #kwargs.pop('object_hook', None) # Remove if user passed one to loads() directly
        super().__init__(object_hook=self.dict_to_object)

    def dict_to_object(self, dct):      
        if 'courses' in dct and isinstance(dct['courses'], list):
            dct['courses'] = set(dct['courses'])
      
       
        return dct   

paylod_message = '''{
    "batch_id": 123,
    "courses": {"X","Y","Z"}, # A set
    "student_names": ["A","B","C"]
}'''
python_obj = json.loads(json_string,cls=CustomSetDecoder)
print(python_obj)


