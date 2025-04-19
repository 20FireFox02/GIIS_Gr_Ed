from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Line_Alg

<<<<<<< HEAD
class Giperb_alg(Algoritm):
    
    def __init__(self):
        self.ret_step()

    def ret_step(self):
        self.step=-1

    def draw_line(self,points,check):
        a=points[1][0]-points[0][0]
        if a != 0:

            x=points[0][0]+abs(a)
            y=points[0][1]

            pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,((2*points[0][0]-x)*PIXEL,y*PIXEL,PIXEL,PIXEL))

            if len(points)<3:
                return
            
            if points[0][1]>points[2][1]:ty=-1
            else:ty=1

            lim=points[2][1]

            if (points[0][0]>=points[1][0] and points[2][0]>=points[1][0]) or (points[0][0]<=points[1][0] and points[2][0]<=points[1][0]):
                while y*ty<lim*ty:
                    check()

                    y+=ty
                    pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
                    pg.draw.rect(display,BLACK,(x*PIXEL,(2*points[0][1]-y)*PIXEL,PIXEL,PIXEL))
                    pg.draw.rect(display,BLACK,((2*points[0][0]-x)*PIXEL,(2*points[0][1]-y)*PIXEL,PIXEL,PIXEL))
                    pg.draw.rect(display,BLACK,((2*points[0][0]-x)*PIXEL,y*PIXEL,PIXEL,PIXEL))
                    
                return
            b2=a**2*(points[2][1]-points[0][1])**2/((points[2][0]-points[0][0])**2-a**2)
            
            delta=b2*(1+2*abs(a))-a**2

            def deqz(x,y,delta):
                return x+1,y+ty,delta+(2*(x-points[0][0])+1)*b2-(2*abs(y-points[0][1])+1)*a**2
            while y*ty<lim*ty:
                check()

                if delta<0:
                    d=2*delta+2*abs(y-points[0][1])*a**2+1
                    if d<=0:
                        x+=1
                        delta=delta+b2*(2*(x-points[0][0])+1)
                    else:x,y,delta=deqz(x,y,delta)
                elif delta>0:
                    d=2*delta-2*(x-points[0][0])*b2-1
                    if d>0:
                        y+=ty
                        delta=delta-a**2*(2*abs(y-points[0][1])+1)
                    else:x,y,delta=deqz(x,y,delta)
                else:x,y,delta=deqz(x,y,delta)
                
                pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,(x*PIXEL,(2*points[0][1]-y)*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((2*points[0][0]-x)*PIXEL,(2*points[0][1]-y)*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((2*points[0][0]-x)*PIXEL,y*PIXEL,PIXEL,PIXEL))


"""def draw_line(self,points,check):
        a=points[1][0]-points[0][0]
        if a != 0:

            pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,((2*points[1][0]-x)*PIXEL,y*PIXEL,PIXEL,PIXEL))

            if len(points)<3:
                return
            
            b=e_crd[1]-b_crd[1]
            lim=e_crd[1]
            
            delta=b**2*(1+2*abs(a))-a**2

            x=b_crd[0]+abs(a)
            y=b_crd[1]

            def deqz(x,y,delta):
                return x+1,y+1,delta+(2*(x-b_crd[0])+1)*b**2-(2*(y-b_crd[1])+1)*a**2
            while y<lim:
                check()
=======
class Giperb_alg(Line_Alg):
    
    def draw_line(self,points,check):

        # Получение заданных точек и значения а
        b_crd,e_crd=points
        a=int((e_crd[0]-b_crd[0])/2)

        # Проверка валидности
        if a != 0:

            # Получение значения b
            b=abs(e_crd[1]-b_crd[1])
            
            # Начальная ошибка и координаты начальной точки
            delta=b**2*(1+2*abs(a))-a**2
            x,y=abs(a),0

            # Отображение начальных точек
            pg.draw.rect(display,BLACK,((x+b_crd[0]+a)*PIXEL,(y+b_crd[1])*PIXEL,PIXEL,PIXEL))
            pg.draw.rect(display,BLACK,((-x+b_crd[0]+a)*PIXEL,(y+b_crd[1])*PIXEL,PIXEL,PIXEL))

            # Двигаемся по диагонали
            def deqz(x,y,delta):return x+1,y+1,delta+(2*x+1)*b**2-(2*y+1)*a**2

            # Выбор ограничения
            if abs(a)<=b:cond=lambda:y<b
            else:cond=lambda:x<a+10

            # Отображение
            while y<b:
>>>>>>> temp-branch

                if delta<0:

                    d=2*delta+2*y*a**2+1
                    if d<=0:

                        # Двигаемся по горизонтали
                        x+=1
                        delta=delta+b**2*(2*x+1)

                    else:x,y,delta=deqz(x,y,delta)
                elif delta>0:

                    d=2*delta-2*x*b**2-1
                    if d>0:

                        # Двигаемся по вертикали
                        y+=1
                        delta=delta-a**2*(2*y+1)

                    else:x,y,delta=deqz(x,y,delta)
                else:x,y,delta=deqz(x,y,delta)
                
<<<<<<< HEAD
                pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,(x*PIXEL,(b_crd[1]-y+b_crd[1])*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((b_crd[0]-x+b_crd[0])*PIXEL,(b_crd[1]-y+b_crd[1])*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((b_crd[0]-x+b_crd[0])*PIXEL,y*PIXEL,PIXEL,PIXEL))"""
=======
                # Отображение полученных точек
                pg.draw.rect(display,BLACK,((x+b_crd[0]+a)*PIXEL,(y+b_crd[1])*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((x+b_crd[0]+a)*PIXEL,(-y+b_crd[1])*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((-x+b_crd[0]+a)*PIXEL,(-y+b_crd[1])*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((-x+b_crd[0]+a)*PIXEL,(y+b_crd[1])*PIXEL,PIXEL,PIXEL))

                # Отладка
                check()
>>>>>>> temp-branch
