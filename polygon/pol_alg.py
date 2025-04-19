from polygon.polygon_module import Edge,Polygon

class Pol_alg():
    def find_pol(points:list)->Polygon:
        return Polygon([Edge([points[n],points[n+1]]) for n in range(-1,len(points)-1,1)])