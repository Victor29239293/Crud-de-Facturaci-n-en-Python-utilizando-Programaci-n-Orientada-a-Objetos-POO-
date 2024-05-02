import json
from utilities import  gotoxy
import time
class JsonFile:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)# dump:graba datos a un archivo json
      
    def read(self):
        try:
            with open(self.filename,'r') as file:
                data = json.load(file)# load:carga datos desde un archivo json
        except FileNotFoundError:
            data = []
        return data
     
    def find(self,atributo,buscado):
        try:
            with open(self.filename,'r') as file:
                datas = json.load(file)
                data =  [item for item in datas if atributo in item and item[atributo] == buscado]
        except FileNotFoundError:
            data = []
        return data
    
    def append(self, new_data):
        existing_data = self.read()
        existing_data.append(new_data)
        self.save(existing_data)
        
    def update(self, key, value, new_data):
        existing_data = self.read()
        updated_data = [item for item in existing_data if item[key] != value]
        updated_data.append(new_data)
        self.save(updated_data)
        
    def update_by_id(self, id_value, new_data):
        existing_data = self.read()
        for i, item in enumerate(existing_data):
            if item['id'] == id_value:
                existing_data[i] = new_data
                break
        self.save(existing_data)
        
    def delete_by_id_or_dni(self, identifier, id_value):
        existing_data = self.read()
        if identifier == 'id':
            updated_data = [item for item in existing_data if item['id'] != id_value]
        elif identifier == 'dni':
            updated_data = [item for item in existing_data if item['dni'] != id_value]
        elif identifier == 'factura':
            updated_data = [item for item in existing_data if item['factura'] != id_value]
        self.save(updated_data)
        
 
   