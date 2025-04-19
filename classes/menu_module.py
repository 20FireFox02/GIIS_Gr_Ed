class Menu:
    def __init__(self,b_crd=[],size=[]):
        self.begin_crd=b_crd
        self.size=size
    def get_end_crd(self,axis:int)->int:
        return self.begin_crd[axis]+self.size[axis]