import numpy as np

from classes.algoritm_module import Curve_Alg
from frst_lines_alg.brezen_alg_module import Brz_alg

MN=np.array([[2,-2,1,1],[-3,3,-2,-1],[0,0,1,0],[1,0,0,0]])

class Herm_inter(Curve_Alg):

    def draw(self, draw_click):
        return super().draw(draw_click)

    def find_points(self,points):
        d=0
        for i in range(len(points)-1):d+=min(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))
        try:d=1/d
        except:d=1
        t=d

        point_o=[points[0]]
        gnx=[points[0],points[2],[points[1][0]-points[0][0],points[1][1]-points[0][1]],\
             [points[3][0]-points[2][0],points[3][1]-points[2][1]]]
        
        while t<=1:
            point=np.matmul(np.array([[t**3,t**2,t,1]]),np.matmul(MN,np.array(gnx)))
            
            Brz_alg().draw_line([[round(point_o[0][0]),round(point_o[0][1])],[round(point[0][0]),round(point[0][1])]],lambda:True)
            point_o=point
            t+=d

    def draw_line(self,points,check):
        
        if len(points)<3:Brz_alg().draw_line(points,lambda:True)
        elif len(points)==3:self.find_points(points+[[2*points[-1][0]-points[-2][0],2*points[-1][1]-points[-2][1]]])
        elif len(points)==4:self.find_points(points)
        else:
            self.find_points(points[:4])
            self.draw_line(points[2:],check)