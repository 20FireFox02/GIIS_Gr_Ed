import math

from wind_init_module import pg,display

from constant_module import WHITE

from mouse_click_module import mouse_click
from drawing.draw_module import draw,draw_menu

from work_envir.work_env_module import work_env
from lab_4.read_file_module import read_file,Cube

T_SPEED,R=math.pi/40,5
SIN_T_P,SIN_T_N,COS_T=math.sin(T_SPEED),math.sin(-T_SPEED),math.cos(T_SPEED)

class work_env_3d(work_env):
    def __init__(self):
        self.T_SPEED=math.pi/40
        self.R=5
        self.SIN_T_P,self.SIN_T_N,self.COS_T=math.sin(self.T_SPEED),math.sin(-self.T_SPEED),math.cos(self.T_SPEED)

        self.a=Cube

    def work(self):
        def draw_disp():
            display.fill(WHITE)
            self.a.draw()
            draw_menu()
        for event in pg.event.get():

            if event.type is pg.QUIT:
                pg.quit()
                exit()

            elif event.type==pg.MOUSEBUTTONDOWN:
                mouse_click(event.pos)
                draw_menu()

            elif event.type==pg.MOUSEWHEEL:
                self.a.scaling(1-event.precise_y)
                draw_disp()
                break
                 
            elif event.type==pg.KEYDOWN:
                if event.key==pg.K_TAB:
                    self.a=read_file("lab_4/figure.txt")
                    draw_disp()
                break
    

        if pg.key.get_pressed()[pg.K_a]:
            self.a.turn_y(self.SIN_T_P,self.COS_T)
            draw_disp()
        elif pg.key.get_pressed()[pg.K_d]:
            self.a.turn_y(self.SIN_T_N,self.COS_T)    
            draw_disp()
        elif pg.key.get_pressed()[pg.K_w]:
            self.a.turn_x(self.SIN_T_P,self.COS_T)
            draw_disp()
        elif pg.key.get_pressed()[pg.K_s]:
            self.a.turn_x(self.SIN_T_N,self.COS_T)
            draw_disp()
        elif pg.key.get_pressed()[pg.K_q]:
            self.a.turn_z(self.SIN_T_P,self.COS_T)    
            draw_disp()
        elif pg.key.get_pressed()[pg.K_e]:
            self.a.turn_z(self.SIN_T_N,self.COS_T)    
            draw_disp()

        elif pg.key.get_pressed()[pg.K_LEFT]:
            self.a.moving(-self.R,0,0)
            draw_disp()
        elif pg.key.get_pressed()[pg.K_RIGHT]:
            self.a.moving(self.R,0,0)
            draw_disp()
        elif pg.key.get_pressed()[pg.K_UP]:
            self.a.moving(0,-self.R,0)
            draw_disp()
        elif pg.key.get_pressed()[pg.K_DOWN]:
            self.a.moving(0,self.R,0)
            draw_disp()
        
        super().work()