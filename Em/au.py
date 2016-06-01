# nom: ActionUnit
class ActionUnit :


    def __init__(self,  id_):
        self.id = id_


    def __str__(self):
        return str(self.id)

au = ActionUnit(666)

print au
