class Line:
<<<<<<< HEAD
    def __init__(self,b_crd,draw_alg):
        self.points=[b_crd]
        self.draw_alg=draw_alg
    
    def new_point(self,point):
        self.points.append(point)
=======
    def __init__(self,points:list,draw_alg:int):
        self.points=points
        self.draw_alg=draw_alg
    def add_point(self,point:list):
        self.points.append(point)
    def upd_point(self,point:list):
        self.points[-1]=point
    def del_point(self):
        self.points.pop()
>>>>>>> temp-branch
