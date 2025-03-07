class Line:
    def __init__(self,b_crd,draw_alg):
        self.points=[b_crd]
        self.draw_alg=draw_alg
    
    def new_point(self,point):
        self.points.append(point)