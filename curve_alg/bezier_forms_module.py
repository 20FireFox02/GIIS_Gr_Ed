import numpy as np

from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Algoritm

from frst_lines_alg.brezen_alg_module import Brz_alg
class Bez_form():
    def draw_line(points,check):
        if len(points)<3:
            Brz_alg.draw_line(points[0],points[1],check)
        def mnb():
            return np.array([[1]+[0 for i in range(len(points)-1)],[0 for i in range(len(points)-1)]+[1]]+\
                            [[0 for j in range(i)]+[-(len(points)-1),len(points)-1]+\
                             [0 for j in range(len(points)-2-i)] for i in range(0,len(points),2)])
        
        def fl_mn():
            return np.linalg.inv(np.array([[0 for i in range(len(points)-1)]+[1],[1 for i in range(len(points))]]+\
                                           [[0 for i in range(len(points)-2)]+[1,0],[i for i in range(len(points)-1,-1,-1)]]))
        
        def mn():
            return np.array([[round(j) for j in i] for i in fl_mn()])
        
        t=0
        while t<=1:
            
            point=np.matmul(np.array([[t**n for n in range(len(points)-1,-1,-1)]]),\
                      np.matmul(np.matmul(mn(),mnb()),np.array([point for point in points])))
            print(point[0])
            pg.draw.rect(display,BLACK,(70+round(point[0][0]*10),round(point[0][1]*10),PIXEL,PIXEL))
            t+=0.1
            check()


#a=Bez_form
#a.draw_line([[0,5],[5,0],[6,6],[3,4]])
'''
A = np.array([[0,0,0,1],[1,1,1,1],[0,0,1,0],[3,2,1,0]])  # Пример матрицы
try:
    A_inv = np.linalg.inv(A)
    print(A_inv)
except np.linalg.LinAlgError:
    print("Обратной матрицы не существует (матрица вырожденная).")'''