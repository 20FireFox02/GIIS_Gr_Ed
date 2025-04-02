from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Line_Alg

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
                
                # Отображение полученных точек
                pg.draw.rect(display,BLACK,((x+b_crd[0]+a)*PIXEL,(y+b_crd[1])*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((x+b_crd[0]+a)*PIXEL,(-y+b_crd[1])*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((-x+b_crd[0]+a)*PIXEL,(-y+b_crd[1])*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((-x+b_crd[0]+a)*PIXEL,(y+b_crd[1])*PIXEL,PIXEL,PIXEL))

                # Отладка
                check()