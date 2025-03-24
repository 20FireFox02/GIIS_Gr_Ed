import numpy as np

from classes.algoritm_module import Algoritm
from frst_lines_alg.brezen_alg_module import Brz_alg

from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Algoritm

class Herm_inter(Algoritm):
    def draw_line(points,check):
       
        d=0
        for i in range(len(points)-1):
            d+=min(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))
            #d+=abs(points[i][0]-points[i+1][0])+abs(points[i][1]-points[i+1][1])
        d=1/d
        t=d

        point_o=[points[0]]
        while t<=1:
            point=np.matmul(np.array([[t**n for n in range(len(points)-1,-1,-1)]]),\
                            np.matmul(np.array([[2,-2,1,1],[-3,3,-2,-1],[0,0,1,0],[1,0,0,0]]),\
                            np.array([point for point in points])))
            
            Brz_alg.draw_line([round(point_o[0][0]),round(point_o[0][1])],[round(point[0][0]),round(point[0][1])],check)
            point_o=point
            #pg.draw.rect(display,BLACK,(round(point[0][0])*PIXEL,round(point[0][1])*PIXEL,PIXEL,PIXEL))
            t+=d