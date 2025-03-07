from wind_init_module import display
from constant_module import WHITE
from drawing.draw_menu_module import draw_menu

from frst_lines_alg.brezen_alg_module import *
from frst_lines_alg.dig_dif_an_module import *
from frst_lines_alg.wu_alg_module import *

from sec_lines_alg.brezen_circle_alg_module import *
from sec_lines_alg.ellipse_alg_module import *
from sec_lines_alg.giperb_alg_module import *
from sec_lines_alg.parab_alg_module import *

from curve_alg.bezier_forms_module import Bez_form

from classes.line_module import Line
lines=[Line([[0,5],[5,0],[6,6],[3,4]],7)]

drawing_alg=[Dda,Brz_alg,Wu_alg,Brz_circle_alg,Ellipse_alg,Giperb_alg,Parab_alg,Bez_form]
"""pg.font.init()
smallfont = pg.font.SysFont('Corbel',25) 
dda_t=smallfont.render('dda',True,BLACK)
brz_t=smallfont.render('brezen',True,BLACK)
wu_t=smallfont.render('wu',True,BLACK)

text=dda_t
"""
def draw(check):
    display.fill(WHITE)
    #draw_menu(display,menu_click)
    draw_menu()
    for line in  lines[:-1]:
        #draw_alg[n].draw_line(display,line[0],line[1],lambda:True)
        #draw_frst_line_alg[n].draw_line(display,line[0],line[1],lambda:True)
        drawing_alg[line.draw_alg].draw_line(line.begin_crd,line.end_crd,lambda:True)
    #draw_alg[n].draw_line(display,lines[-1][0],lines[-1][1],check)
    #drawing_alg[lines[-1].draw_alg].draw_line(lines[-1].begin_crd,lines[-1].end_crd,lambda:True)
    drawing_alg[lines[-1].draw_alg].draw_line(lines[-1].points,check)
    try:
        #draw_alg[n].draw_line(display,lines[-1][0],lines[-1][1],check)
        #draw_frst_line_alg[n].draw_line(display,lines[-1][0],lines[-1][1],check)
        #drawing_alg[lines[-1].draw_alg].draw_line(lines[-1].begin_crd,lines[-1].end_crd,check)
        drawing_alg[lines[-1].draw_alg].draw_line(lines[-1].points,check)
    except:
        print("Error last line drawing")
    draw_menu()