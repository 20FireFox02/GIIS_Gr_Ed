from abc import ABCMeta, abstractmethod

class Algoritm():
    __metaclass__=ABCMeta

    @abstractmethod
    def draw_line(points:list,check):
        pass
    
    @abstractmethod
    def draw(draw_click:bool):
        pass

class Curve_Alg(Algoritm):
    def draw_line(points, check):
        pass
    def draw(self,draw_click):
        return True

class Line_Alg(Algoritm):
    def draw_line(points, check):
        pass
    def draw(draw_click):
        return not draw_click
