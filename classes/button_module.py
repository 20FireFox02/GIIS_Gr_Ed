class Button:
    def __init__(self,b_crd,size,command):
        self.begin_crd=b_crd
        self.size=size
        self.command=command
    def click(self):
        self.command()
    def get_end_crd(self,axis):
        return self.begin_crd[axis]+self.size[axis]