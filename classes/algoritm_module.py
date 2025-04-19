from abc import ABCMeta, abstractmethod
from classes.line_module import Line

class Algoritm():
    __metaclass__=ABCMeta

    @abstractmethod
<<<<<<< HEAD
    def draw_line():
        pass
=======
    def draw_line(points:list,check):
        pass
    
    @abstractmethod
    def draw(draw_click:bool):
        pass

    @abstractmethod
    def add_point(line:Line,point:list):
        pass

class Curve_Alg(Algoritm):
    def draw_line(points:list, check):
        pass
    def draw(self,draw_click:bool)->bool:
        return True
    def add_point(self,line:Line,point:list):
        line.add_point(point)

class Line_Alg(Algoritm):
    def draw_line(points, check):
        pass
    def draw(self,draw_click:bool)->bool:
        return not draw_click
    def add_point(self,line:Line, point:list):
        line.upd_point(point)
>>>>>>> temp-branch
