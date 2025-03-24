import numpy as np

from classes.algoritm_module import Curve_Alg

from frst_lines_alg.brezen_alg_module import Brz_alg

MB3=np.array([[1,-2,1],[-2,2,0],[1,0,0]])
MB4=np.array([[-1,3,-3,1],[3,-6,3,0],[-3,3,0,0],[1,0,0,0]])

class Bez_form(Curve_Alg):
    
    def draw(self,draw_click):
        return super().draw(draw_click)
    
    def find_points(self,points,mb,check):
        d=0
        for i in range(len(points)-1):d+=min(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))
        try:d=1/d
        except:d=1
        t=d
        point_o=[points[0]]

        while t<=1:
            point=np.matmul(np.array([[t**n for n in range(len(points)-1,-1,-1)]]),\
                      np.matmul(mb,np.array([point for point in points])))
            Brz_alg.draw_line([round(point_o[0][0]),round(point_o[0][1])],[round(point[0][0]),round(point[0][1])],check)
            point_o=point
            t+=d
        Brz_alg.draw_line([round(point_o[0][0]),round(point_o[0][1])],[round(points[-1][0]),round(points[-1][1])],check)


    def draw_line(self,points,check):
        
        if len(points)<3:Brz_alg.draw_line(points[0],points[1],check)
        elif len(points)==3:self.find_points(points,MB3,check)
        elif len(points)==4:self.find_points(points,MB4,check)
        else:
            self.find_points(points[:4],MB4,check)
            self.draw_line([points[3]]+[[2*points[3][0]-points[2][0],2*points[3][1]-points[2][1]]]+points[4:],check)
            
        


#a=Bez_form
#a.draw_line([[0,5],[5,0],[6,6],[3,4]])
'''
A = np.array([[0,0,0,1],[1,1,1,1],[0,0,1,0],[3,2,1,0]])  # Пример матрицы
try:
    A_inv = np.linalg.inv(A)
    print(A_inv)
except np.linalg.LinAlgError:
    print("Обратной матрицы не существует (матрица вырожденная).")
    
    [t4 t3 t2 t1 t0]  [5x5]   [P1 P2 P3 P4 P5]
    '''


'''def mnb():
            return np.array([[1]+[0 for i in range(len(points)-1)],[0 for i in range(len(points)-1)]+[1]]+\
                            [[0 for j in range(i)]+[-(len(points)-1),len(points)-1]+\
                             [0 for j in range(len(points)-2-i)] for i in range(0,len(points),2)])
        
        def fl_mn():
            return np.linalg.inv(np.array([[0 for i in range(len(points)-1)]+[1],[1 for i in range(len(points))]]+\
                                           [[0 for i in range(len(points)-2)]+[1,0],[i for i in range(len(points)-1,-1,-1)]]))
        
        def mn():
            return np.array([[round(j) for j in i] for i in fl_mn()])'''

'''point_o=np.matmul(np.array([[0**n for n in range(len(points)-1,-1,-1)]]),\
                      np.matmul(mb,np.array([point for point in points])))'''