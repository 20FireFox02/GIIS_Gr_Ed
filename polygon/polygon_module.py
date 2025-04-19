from frst_lines_alg.brezen_alg_module import Brz_alg

X=1000

class Edge():
    def __init__(self,points:list):
        self.p_1,self.p_2=points
    def get_v_x(self):
        return self.p_2[0]-self.p_1[0]
    def get_v_y(self):
        return self.p_2[1]-self.p_1[1]
    def get(self):
        return [self.p_1,self.p_2]

class Polygon():
    def __init__(self,edges:list):
        self.edges=edges

    def draw_pol(self):
        for edge in self.edges:
            Brz_alg().draw_line([edge.p_1,edge.p_2],lambda:True)
        # n=-2
        # n_v=self.fing_norm(n)
        # Brz_alg().draw_line([self.edges[n].p_1,[self.edges[n].p_1[0]+n_v[0],self.edges[n].p_1[1]+n_v[1]]],lambda:True)

    def convex_check(self)->bool:
        v_p=[(self.edges[n].get_v_y()*self.edges[n-1].get_v_x()-\
              self.edges[n].get_v_x()*self.edges[n-1].get_v_y()) for n in range(len(self.edges))]
        if v_p[0]>0:
            for p in v_p[1:]:
                if p<0:return False
        elif v_p[0]<0:
            for p in v_p[1:]:
                if p>0:return False
        return True

    def fing_norm(self,n:int)->list:
        if 0>self.edges[n].get_v_x()*(self.edges[n+1].p_2[1]-self.edges[n].p_1[1])-\
                    self.edges[n].get_v_y()*(self.edges[n+1].p_2[0]-self.edges[n].p_1[0]):
        # if 0>self.edges[n].get_v_x()*(self.edges[n+1].p_2[0]-self.edges[n].p_1[0])+\
        #     (self.edges[n+1].p_2[1]-self.edges[n].p_1[1])*self.edges[n].get_v_y():
            return [self.edges[n].get_v_y(),-self.edges[n].get_v_x()]
        return [-self.edges[n].get_v_y(),self.edges[n].get_v_x()]
    
    def find_int_point(self,line):
        int_points=[]
        p1,p2=line
        d=[p2[0]-p1[0],p2[1]-p1[1]]
        
        # n=-2
        # if True:
        for n in range(-2,len(self.edges)-2):
            n_v=self.fing_norm(n)
            #print(self.edges[n].p_1,self.edges[n].p_2)
            f=self.edges[n].p_1
            w=[p1[0]-f[0],p1[1]-f[1]]
            #print(f)
            #print(n_v)
            try:
                t=-(n_v[0]*w[0]+n_v[1]*w[1])/(n_v[0]*d[0]+n_v[1]*d[1])
                #t=-(n_v[0]*(p1[0]-f[0])+n_v[1]*(p1[1]-f[1]))/(n_v[0]*(p2[0]-p1[0])+n_v[1]*(p2[1]-p1[1]))
                #print(t)
                x=p1[0]+int((p2[0]-p1[0])*t)
                y=p1[1]+int((p2[1]-p1[1])*t)
                if 0<=t<=1:
                    #print([x,y])
                    try:
                        if not 0<=(x-f[0])/(self.edges[n].p_2[0]-f[0])<=1:
                            #return int_points
                            continue
                    except:pass
                    try:
                        if not 0<=(y-f[1])/(self.edges[n].p_2[1]-f[1])<=1:
                                #return int_points 
                                continue
                    except:pass
                    #print(t)
                    #print(p1[0]+round((p2[0]-p1[0])*t),p1[1]+round((p2[1]-p1[1])*t))
                    int_points.append([x,y])
            except:
                pass
            
            #step=1/(max(abs(self.edges[i].get_v_x()),abs(self.edges[i].get_v_y())))
            #print(i)
            '''t=0
            while t<=1:
                f=[self.edges[i].p_1[0]+round((self.edges[i].p_2[0]-self.edges[i].p_1[0])*t),\
                   self.edges[i].p_1[1]+round((self.edges[i].p_2[1]-self.edges[i].p_1[1])*t)]
                w=[line[0][0]-f[0],line[0][1]-f[1]]
                #print((d[0]**2+d[1]**2)*(w[0]**2+w[1]**2))
                #print((w[0]*d[0]+w[1]*d[1])/(((d[0]**2+d[1]**2)*(w[0]**2+w[1]**2))**0.5))
                if abs((w[0]*d[0]+w[1]*d[1])/(((d[0]**2+d[1]**2)*(w[0]**2+w[1]**2))**0.5))==1:
                    print(f)
                    int_points.append(f)
                print((n_v[0]*(line[0][0]-f[0])+n_v[1]*(line[0][1]-f[1]))/\
                    (n_v[0]*(line[1][0]-line[0][0])+n_v[1]*(line[1][1]-line[0][1])))
                print(f)'''
            '''if ((n_v[0]*(line[0][0]-f[0])+n_v[1]*(line[0][1]-f[1]))/\
                    (n_v[0]*(line[1][0]-line[0][0])+n_v[1]*(line[1][1]-line[0][1])))==0:
                    print(f)
                t+=step'''
        '''step=1/(line[1][0]-line[0][0])
        t=0
        while t<=1:
            point=[line[0][0]+round((line[1][0]-line[0][0])*t),line[0][1]+round((line[1][1]-line[0][1])*t)]
            for n in range(-2,len(self.edges)-2):
                v_n=self.fing_norm(n)
                if v_n[0]*(self.edges[n].p_1[0]-point[0])+(self.edges[n].p_1[1]-point[1])*v_n[1]==0:
                    if 0<=(point[0]-self.edges[n].p_1[0])/(self.edges[n].get_v_x())<=1 and\
                        0<=(point[1]-self.edges[n].p_1[1])/(self.edges[n].get_v_y())<=1:
                        return True
            t+=step'''
        return int_points
    
    def find_point(self,x:int,y:int)->bool:
        #print(x,y)
        #print((self.find_int_point([[x,y],[X,y]])))
        if len(self.find_int_point([[x,y],[X,y]]))%2!=0:
            if self.convex_check():
                print('ВЫПУКЛЫЙ')
            else:
                print('ВОГНУТЫЙ')
            return True
        else:
            return False


#a=Polygon([Edge([[0,0],[2,0]]),Edge([[2,0],[2,2]]),Edge([[2,2],[0,2]]),Edge([[0,2],[0,0]])])
#print(a.find_int_point([[2,-1],[4,1]]))