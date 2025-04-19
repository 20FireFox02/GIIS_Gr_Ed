import numpy as np

from frst_lines_alg.brezen_alg_module import Brz_alg

D=50

class Cube():

    def __init__(self,points:list):
        self.points=[points[:3],[points[0]+points[3],points[1],points[2]],[points[0],points[1]+points[3],points[2]],\
                     [points[0],points[1],points[2]+points[3]],[points[0]+points[3],points[1]+points[3],points[2]],\
                        [points[0]+points[3],points[1],points[2]+points[3]],[points[0],points[1]+points[3],points[2]+points[3]],\
                            [points[0]+points[3],points[1]+points[3],points[2]+points[3]]]
        c=points[3]/2
        self.center=[points[0]+c,points[1]+c,points[2]+c,1]
        self.edge=[[1,2,3],[4,5],[4,6],[5,6],[7],[7],[7],[]]
        print(self.points)

    def draw(self):
        
        for n,point_1 in enumerate(self.points):
            for point_2 in self.edge[n]:
                Brz_alg().draw_line([[(round(point_1[0]-500)/(point_1[2]/D)+500),round((point_1[1]-400)/(point_1[2]/D)+400)],\
                                     [round((self.points[point_2][0]-500)/(self.points[point_2][2]/D)+500),\
                                      round((self.points[point_2][1]-400)/(self.points[point_2][2]/D)+400)]],lambda:True)
    
    def turn_x(self,sin:float,cos:float):
        self.turn(np.array([[1,0,0,0],[0,cos,-sin,0],[0,sin,cos,0],[0,0,0,1]]))

    def turn_y(self,sin:float,cos:float):
        self.turn(np.array([[cos,0,-sin,0],[0,1,0,0],[sin,0,cos,0],[0,0,0,1]]))

    def turn_z(self,sin:float,cos:float):
        self.turn(np.array([[cos,-sin,0,0],[sin,cos,0,0],[0,0,1,0],[0,0,0,1]]))

    def turn(self,mtr):
        pnt=np.array([[point[0]-self.center[0],point[1]-self.center[1],point[2]-self.center[2],1] for point in self.points])
        self.points=[[point[0]+self.center[0],point[1]+self.center[1],point[2]+self.center[2]] for point in np.matmul(pnt,mtr)]

    def moving(self,dx:int,dy:int,dz:int):
        mtr=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[dx,dy,dz,1]])
        pnt=np.array([[point[0],point[1],point[2],1] for point in self.points])
        self.points=[point[:3] for point in np.matmul(pnt,mtr)]
        self.center=np.matmul(np.array([self.center]),mtr)[0]

    def scaling(self,s:float):
        mtr=np.array([[s,0,0,0],[0,s,0,0],[0,0,s,0],[0,0,0,1]])
        pnt=np.array([[point[0]-self.center[0],point[1]-self.center[1],point[2]-self.center[2],1] for point in self.points])
        self.points=[[point[0]+self.center[0],point[1]+self.center[1],point[2]+self.center[2]] for point in np.matmul(pnt,mtr)]

        
        '''for i,point in enumerate(self.points):
            a=[0,0,0,0]
            for n,col in enumerate(m):
                a[n]+=col[0]*(point[0]-100)+col[1]*(point[1]-80)+col[2]*(point[2]-20)+col[3]
            self.points[i]=[a[0]+100,a[1]+80,a[2]+20]
            print(a)
            print(a[3])'''

        


''' mtr=np.array([[1,0,0,0],[0,cos,sin,0],[0,-sin,cos,0],[0,0,0,1]])
        pnt=np.array([[point[0]-100,point[1]-80,point[2]-20,1] for point in self.points])
        self.points=[[point[:3][0]+100,point[:3][1]+80,point[3]+20] for point in np.matmul(pnt,mtr)]'''

'''mtr=np.array([[cos,sin,0],[-sin,cos,0],[0,0,1]])
        pnt=np.array([[point[0]-100,point[1]-80,1] for point in self.points])
        self.points=[[point[0]+100,point[1]+80] for point in np.matmul(pnt,mtr)]'''

'''mtr=np.array([[cos,sin,0,0],[-sin,cos,0,0],[0,0,1,0],[0,0,0,1]])
        pnt=np.array([[point[0]-100,point[1]-80,point[2]-20,1] for point in self.points])
        self.points=[[point[:3][0]+100,point[:3][1]+80,point[3]+20] for point in np.matmul(pnt,mtr)]'''

'''def __init__(self,points:list):
        self.points=points
        mx,mn=points[0],points[0]
        for point in points[1:]:
            mx=[max(mx[0],point[0]),max(mx[1],point[1]),max(mx[2],point[2])]
            mn=[min(mn[0],point[0]),min(mn[1],point[1]),min(mn[2],point[2])]
        self.center=[(mx[0]-mn[0])/2+mn[0],(mx[1]-mn[1])/2+mn[1],(mx[2]-mn[2])/2+mn[2]]
        print(self.center)'''