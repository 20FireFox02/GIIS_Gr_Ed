import math
from polygon.polygon_module import Edge,Polygon

class Djarw_alg():
    
    def find_pol(points:list)->Polygon:

        def tan(t:list,point:list)->float:            
            try:
                f=math.atan((point[1]-t[1])/(point[0]-t[0]))
                if t[0]>point[0]:f+=math.pi
                return f
            except:
                return math.pi/2
            
        p,m=points[0],points[0]
        for point in points[1:]:
            if point[1]<p[1]:
                p=point
            elif point[1]>m[1]:m=point
        points.remove(p)
        '''m=points[0]
        for point in points[1:]:
             if point[1]>m[1]:m=point'''
        
        t=[p]
        p_points=[]
        while t[-1]!=m:
            f_n=tan(t[-1],points[0])
            t.append(points[0])
            for point in points[1:]:
                f=tan(t[-2],point)
                if f<f_n:
                    t[-1]=point
                    f_n=f
            points.remove(t[-1])
            p_points.append(Edge([t[-2],t[-1]]))
        #print([point.get() for point in p_points])
        points.append(p)
        while t[-1]!=p:
            f_n=tan([-t[-1][0],-t[-1][1]],[-points[0][0],-points[0][1]])
            t.append(points[0])
            for point in points[1:]:
                f=tan([-t[-2][0],-t[-2][1]],[-point[0],-point[1]])
                if f<f_n:
                    t[-1]=point
                    f_n=f
            points.remove(t[-1])
            p_points.append(Edge([t[-2],t[-1]]))
        #print([point.get() for point in p_points])

        return Polygon(p_points)
    
#Djarw_alg.find_pol([[12,4],[7,10],[10,20],[12,12],[16,12],[21,16],[21,12]])