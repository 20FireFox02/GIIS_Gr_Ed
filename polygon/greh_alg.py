import math
from polygon.polygon_module import Edge,Polygon

class Greh_alg():
    def find_pol(points:list)->Polygon:
        def tan(point):            
            try:
                f=math.atan((point[1]-p[1])/(point[0]-p[0]))
                if f<0:f+=math.pi
                return f
            except:
                return math.pi/2
        
        def shell_build(p_points:list,points:list):
            if not points:
                p_points.append(Edge([p_points[-1].p_2,p_points[0].p_1]))
            
            elif (p_points[-1].get_v_x())*(points[0][1]-p_points[-1].p_2[1])\
                -(p_points[-1].get_v_y())*(points[0][0]-p_points[-1].p_2[0])>0:
                p_points.append(Edge([p_points[-1].p_2,points[0]]))
                #print([point.get() for point in p_points])
                shell_build(p_points,points[1:])
                
            else:
                p_points.pop()
                #print([point.get() for point in p_points])
                shell_build(p_points,points)
            
        p=points[0]
        for point in points[1:]:
            if point[1]<p[1]:
                p=point
        points.remove(p)
        points.sort(key=lambda point: tan(point))
        #print(points)
        p_points=[Edge([p,points[0]])]
        shell_build(p_points,points[1:])
        return Polygon(p_points)
        

        
#Greh_alg.find_pol([[12,4],[7,10],[10,20],[12,12],[16,12],[21,16],[21,12]])

'''(p_points[-1][0]-p_points[-2][0])*(points[0][1]-p_points[-1][1])\
                -(p_points[-1][1]-p_points[-2][1])*(points[0][0]-p_points[-1][0])>0'''