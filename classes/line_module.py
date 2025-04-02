class Line:
    def __init__(self,points:list,draw_alg:int):
        self.points=points
        self.draw_alg=draw_alg
    def add_point(self,point:list):
        self.points.append(point)
    def upd_point(self,point:list):
        self.points[-1]=point
    def del_point(self):
        self.points.pop()