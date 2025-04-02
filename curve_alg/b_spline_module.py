import numpy as np

from classes.algoritm_module import Curve_Alg
from frst_lines_alg.brezen_alg_module import Brz_alg

MS=np.array([[-1,3,-3,1],[3,-6,3,0],[-3,0,3,0],[1,4,1,0]])

class B_spl(Curve_Alg):
    
    def find_points(self,points,point_o):

        # Нахождение шага
        d=0
        for i in range(len(points)-1):d+=min(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))
        try:d=1/d
        except:d=1

        t=0

        # Нахождение точек
        while t<=1:
            point=np.matmul(np.array([[t**3,t**2,t,1]]),\
                    np.matmul(MS,np.array([point for point in points])))/6

            # Построение отрезка  
            Brz_alg().draw_line([[round(point_o[0][0]),round(point_o[0][1])],[round(point[0][0]),round(point[0][1])]],lambda:True)
            point_o=point
            t+=d
        return point_o


    def draw_line(self,points,check):
        
        # Задано 2 точки -- построение отрезка
        if len(points)<3:Brz_alg().draw_line(points,lambda:True)

        # Задано 3 точки -- обавление точки
        elif len(points)==3:self.find_points([points[0],points[1],points[2],\
                                              [2*points[2][0]-points[1][0],2*points[2][1]-points[1][1]]],[points[0]])
            
        # Заданно 4 и более
        else:
            point_o=[points[0]]

            # Построение секции
            for i in range(len(points)-3):
                point_o=self.find_points([point for point in points[i:i+4]],point_o)
            '''Brz_alg().draw_line([[round(point_o[0][0]),round(point_o[0][1])],\
                                 [round([points[-1]][0][0]),round([points[-1]][0][1])]],lambda:True)'''