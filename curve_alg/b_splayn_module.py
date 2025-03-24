import numpy as np

from classes.algoritm_module import Curve_Alg

from frst_lines_alg.brezen_alg_module import Brz_alg
class B_spl(Curve_Alg):
    def draw(self, draw_click):
        return super().draw(draw_click)
    
    def find_points(self,points,mb,check):
        d=0
        for i in range(len(points)-1):
            d+=min(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))
            #d+=abs(points[i][0]-points[i+1][0])+abs(points[i][1]-points[i+1][1])
        try:d=1/d
        except:d=1
        t=d
        point_o=[points[0]]

        for i in range(len(points)-3):
            while t<=1:
                point=np.matmul(np.array([[t**n for n in range(len(points)-1,-1,-1)]]),\
                        np.matmul(mb,np.array([point for point in points[i:i+4]])))/6
                Brz_alg.draw_line([round(point_o[0][0]),round(point_o[0][1])],[round(point[0][0]),round(point[0][1])],check)
                point_o=point
                t+=d
            #check()
            #Brz_alg.draw_line([round(point_o[0][0]),round(point_o[0][1])],[round(points[-1][0]),round(points[-1][1])],check)

    def draw_line(self,points,check):
        
        if len(points)<3:Brz_alg.draw_line(points[0],points[1],check)
        elif len(points)==3:pass#self.find_points(points,np.array([[1,-2,1],[-2,2,0],[1,0,0]]),check)
        else:self.find_points(points,np.array([[-1,3,-3,1],[3,-6,3,0],[-3,0,3,0],[1,4,1,0]]),check)