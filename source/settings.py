import json

from typing import Any 


class Settings :

    def __init__(self, path = 'assets/app.json') -> None : 

        self.path = path

        with open(self.path, 'r', encoding="utf8") as r_settings :
            
            self.raw = dict(json.load(r_settings))

        for key, value in self.raw.items() :             
            if key != 'settings' :
                self.__setattr__(key, value)
            else :
                self.settings = dict(value)

    def update(self, settings : dict) : 
        
        self.settings = settings 
        self.raw['settings'] = self.settings

        with open(self.path, 'w', encoding='utf8') as w_settings : 
            json.dump(self.raw, w_settings)