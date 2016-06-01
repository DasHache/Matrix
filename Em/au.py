from au_dict import au_dict

class ActionUnits :
    dict = au_dict
    
    def __init__(self):
        pass

    def __str__(self):
        return str(self.dict)

    def __getitem__(self, index):
        return self.dict[index]
        
